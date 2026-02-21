import numpy as np

class Part:
    def __init__(self, L, W, H):
        if L % 2 != 0 or H % 2 != 0:
            raise ValueError("零件尺寸 L, W, H 必须为偶数")
        if W * 2 >= H:
            raise ValueError("零件宽度 W 必须小于高度 H 的一半")
        if W * 2 == L:
            raise ValueError("零件宽度 W 不得等于长度 L 的一半")
        self.L = L
        self.W = W
        self.H = H

    def create_all_parts(self):
        """
        生成所有可能的零件形状。
        假设零件是 H x W x L 的长方体 (注意方向可能需要根据实际坐标系调整)
        对于经典的鲁班锁，通常只考虑中间交叉区域的体素是否移除。
        
        返回:
            list of np.ndarray: 每个元素是一个表示零件的三维数组 (0表示空，1表示实体)
        """
        # 1. 初始化完整零件
        # 假设零件沿 X 轴放置，也就是长度为 H
        # 尺寸为 (H, W, L)
        full_part = np.ones((self.H, self.W, self.L), dtype=int)
        
        # 2. 确定可开槽区域
        # 通常是中间的部分。长度方向中间 self.L (或其他零件的宽度) 长度的区域。
        # 这里假设 L 和 W 是另外两组零件的截面尺寸，所以交叉区域的长度也是 W 或 L。
        # 为了简单起见，假设标准鲁班锁，中间区域长度为 2 (即 L 或 W 的值)
        
        center_x = self.H // 2
        # 开槽区域长度，通常等于其他零件的宽度，这里假设都是 W (即2)
        # 范围从 center_x - W//2 到 center_x + W//2
        notch_region_start = center_x - self.W // 2
        notch_region_end = center_x + self.W // 2

        # 在截面上 (W x L)，除了保持零件连通性的核心部分外，其他都可以挖去。
        # 但标准的做法是考虑所有可能的 1x1x1 体素移除组合，只要不把零件断开。
        
        # 获取开槽区域的所有坐标
        notch_coords = []
        for x in range(notch_region_start, notch_region_end):
            for y in range(self.W):
                for z in range(self.L):
                    notch_coords.append((x, y, z))
        
        # 3. 生成所有组合
        # 这里的组合数量是 2^(W * L * notch_length)。对于 2x2x2，就是 2^8 = 256 种。
        # 如果是 2x2x2 的中间区域，共有 8 个体素。
        
        all_parts = []
        num_notch_voxels = len(notch_coords)
        
        # 遍历所有可能的开槽状态 (0 到 2^n - 1)
        # 用位运算来决定每个体素是否存在
        # 注意：这里会生成极其大量的零件，如果是 2x2x2=8个位置，256种，还可以。
        # 但如果是更复杂的区域，可能需要限制。
        
        total_combinations = 1 << num_notch_voxels
        
        for i in range(total_combinations):
            part = full_part.copy()
            valid_part = True
            
            # 根据位掩码挖去体素
            for j in range(num_notch_voxels):
                if (i >> j) & 1:
                    # 如果对应位是 1，表示这个位置被挖掉 (设为0)
                    cx, cy, cz = notch_coords[j]
                    part[cx, cy, cz] = 0
            
            # 4. 验证零件有效性 (可选)
            # 比如检查零件是否断裂。简单的检查是看两端是否连通。
            if self.is_connected(part):
                all_parts.append(part)
                
        return all_parts

    def is_connected(self, part):
        """
        检查零件是否连通 (未断裂)。
        简单的连通性检查：使用泛洪填充或并查集。
        这里我们关心的是左端 (x=0) 和右端 (x=H-1) 是否通过实体体素相连。
        """
        from scipy.ndimage import label
        
        # 标记连通区域 (默认对角线不连通，结构元素用默认即可)
        labeled_array, num_features = label(part)
        
        if num_features == 0:
            return False
            
        # 检查两端是否属于同一个连通分量
        # 获取左端面所有实体像素的标签
        left_labels = np.unique(labeled_array[0, :, :])
        left_labels = left_labels[left_labels != 0] # 去除背景0
        
        # 获取右端面所有实体像素的标签
        right_labels = np.unique(labeled_array[-1, :, :])
        right_labels = right_labels[right_labels != 0]
        
        # 如果左端和右端有共同的标签，说明连通
        return not set(left_labels).isdisjoint(set(right_labels))

if __name__ == "__main__":
    L = 2
    W = 2
    H = 6
    generator = Part(L, W, H)
    parts = generator.create_all_parts()
    print(f"生成的零件总数: {len(parts)}")