import os
import subprocess

# OpenSCAD 路径配置
OPENSCAD_EXE = r"C:\Program Files\OpenSCAD\openscad.exe"


class SixPieceBurrPuzzleShow:
    def __init__(self, L, W, H, unit_cube = 5):
        self.L = L
        self.W = W
        self.H = H
        self.unit_cube = unit_cube
        self.max_dim = max(L, 2 * W, H)
        self.whole_space = self.init_space()
        # 零件生成基本参数
        self.parts = {
            'A': {'color': [1, 0, 0, 0.85], 'fill_param': (0, 1, 2, 1), 'offset': (0, 1, 0)}, # 零件A: 红
            'B': {'color': [0, 0.8, 0, 0.85], 'fill_param': (0, 1, 2, -1), 'offset': (0, -1, 0)}, # 零件B: 绿
            'C': {'color': [0, 0.4, 1, 0.85], 'fill_param': (1, 2, 0, 1), 'offset': (0, 0, 1)}, # 零件C: 蓝
            'D': {'color': [1, 0.8, 0, 0.85], 'fill_param': (1, 2, 0, -1), 'offset': (0, 0, -1)}, # 零件D: 黄
            'E': {'color': [1, 0.4, 0, 0.85], 'fill_param': (2, 0, 1, 1), 'offset': (1, 0, 0)}, # 零件E: 橙
            'F': {'color': [0.6, 0, 1, 0.85], 'fill_param': (2, 0, 1, -1), 'offset': (-1, 0, 0)}, # 零件F: 紫
            'public': {'color': [0.8, 0.8, 0.8, 0.85], 'fill_param': None, 'offset': (1, 1, 1)} # 公共区域 灰
        }

    # 检查尺寸是否合法
    def validate_dimensions(self):
        if not all(isinstance(x, int) for x in [self.L, self.W, self.H]):
            raise ValueError("零件尺寸 L, W 和 H 必须全部为整数")
        if self.L % 2 != 0 or self.W % 2 != 0 or self.H % 2 != 0:
            raise ValueError("零件尺寸 L, W 和 H 必须全部为偶数")

    # 初始化三维数组
    def init_space(self):
        return [[[[] for _ in range(self.max_dim)] for _ in range(self.max_dim)] for _ in range(self.max_dim)]

    # 遍历构建零件
    def build_parts(self):
        for part_name, part_info in self.parts.items():
            if part_info['fill_param'] is None:
                continue
            param = part_info['fill_param']
            for l in range(self.max_dim // 2 - self.L // 2, self.max_dim // 2 + self.L // 2):
                for w in range(self.max_dim // 2 + min(0, param[3] * self.W), self.max_dim // 2 + max(0, param[3] * self.W)):
                    for h in range(self.max_dim // 2 - self.H // 2, self.max_dim // 2 + self.H // 2):
                        idx = [0, 0, 0]
                        idx[param[0]] = l # H方向
                        idx[param[1]] = w # W方向
                        idx[param[2]] = h  # L方向
                        self.whole_space[idx[0]][idx[1]][idx[2]].append(part_name)

    def create_scad_file(self, filename):
        with open(filename, 'w') as f:
            f.write("// SCAD file for Six Piece Burr Puzzle\n")
            
            # 偏移量，用于展示单独的零件 (根据零件方向设置偏移)
            offset_dist = 1.5 * self.max_dim * self.unit_cube
            offset_map = {}
            for part_name, part_info in self.parts.items():
                if part_info['fill_param'] is not None and 'offset' in part_info:
                    offset_dir = part_info['offset']
                    offset_map[part_name] = [offset_dir[0] * offset_dist, offset_dir[1] * offset_dist, offset_dir[2] * offset_dist]
            
            # 增加公共区域的偏移
            if 'public' in self.parts:
                offset_dir = self.parts['public']['offset']
                offset_map['public'] = [offset_dir[0] * offset_dist, offset_dir[1] * offset_dist, offset_dir[2] * offset_dist]
            # --- 1. 整体零件 ---
            f.write("// 整体模型\n")
            f.write("union() {\n")
            for z in range(self.max_dim):
                for y in range(self.max_dim):
                    for x in range(self.max_dim):
                        cell_parts = self.whole_space[x][y][z]
                        if not cell_parts:
                            continue

                        # 如果有多个零件占用同一位置，判定为公共区域
                        is_public = len(cell_parts) > 1
                        
                        # 显示颜色：如果是公共区域，用灰色；否则用零件颜色
                        color = self.parts['public']['color'] if is_public else self.parts[cell_parts[0]]['color']
                        
                        # 写入整体模型的体素
                        f.write(f"  translate([{x * self.unit_cube}, {y * self.unit_cube}, {z * self.unit_cube}]) ")
                        f.write(f"color([{color[0]}, {color[1]}, {color[2]}, {color[3]}]) cube([{self.unit_cube}, {self.unit_cube}, {self.unit_cube}]);\n")
            f.write("}\n\n")

            # --- 2. 零件分开打印 (每个零件用 union 包裹) ---
            # 先按零件名收集体素
            part_voxels = {}
            for z in range(self.max_dim):
                for y in range(self.max_dim):
                    for x in range(self.max_dim):
                        cell_parts = self.whole_space[x][y][z]
                        if not cell_parts:
                            continue
                        
                        is_public = len(cell_parts) > 1
                        if is_public:
                            part_voxels.setdefault('public', []).append((x, y, z))
                        else:
                            part_name = cell_parts[0]
                            if part_name in offset_map:
                                part_voxels.setdefault(part_name, []).append((x, y, z))

            # 逐个零件写入 union
            for part_name, voxels in part_voxels.items():
                color = self.parts[part_name]['color']
                offset = offset_map[part_name]
                f.write(f"// 零件 {part_name}\n")
                f.write("union() {\n")
                for (x, y, z) in voxels:
                    f.write(f"  translate([{x * self.unit_cube + offset[0]}, {y * self.unit_cube + offset[1]}, {z * self.unit_cube + offset[2]}]) ")
                    f.write(f"color([{color[0]}, {color[1]}, {color[2]}, {color[3]}]) cube([{self.unit_cube}, {self.unit_cube}, {self.unit_cube}]);\n")
                f.write("}\n\n")

    def render_png(self, scad_path, png_path):
        """调用 OpenSCAD 命令行将 SCAD 渲染为 PNG"""
        if not os.path.isfile(OPENSCAD_EXE):
            print(f"[WARN] 找不到 OpenSCAD: {OPENSCAD_EXE}，跳过 PNG 渲染。")
            return

        cmd = [
            OPENSCAD_EXE,
            "-o", png_path,
            "--autocenter",
            "--viewall",
            "--imgsize", "2048,1536",
            "--colorscheme", "Tomorrow Night",
            scad_path,
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            print(f"[WARN] OpenSCAD 返回码 {result.returncode}")
            if result.stderr:
                for line in result.stderr.strip().splitlines()[:5]:
                    print(f"       {line}")

if __name__ == "__main__":
    L = 10
    W = 2
    H = 10
    puzzle_show = SixPieceBurrPuzzleShow(L, W, H)
    puzzle_show.validate_dimensions()
    puzzle_show.build_parts()
    scad_file = f"scad\\six_piece_burr_puzzle_show_{L}_{W}_{H}.scad"
    puzzle_show.create_scad_file(scad_file)
    png_file = f"image\\six_piece_burr_puzzle_show_{L}_{W}_{H}.png"
    puzzle_show.render_png(scad_file, png_file)