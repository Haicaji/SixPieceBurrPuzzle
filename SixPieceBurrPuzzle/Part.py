import numpy as np

class Part:
    def __init__(self, L, W, H):
        self.L = L
        self.W = W
        self.H = H
        [self.min, self.mid, self.max] = sorted([self.L, 2*self.W, self.H])

    # 检查尺寸是否合法
    def validate_dimensions(self):
        if not all(isinstance(x, int) for x in [self.L, self.W, self.H]):
            raise ValueError("零件尺寸 L, W 和 H 必须全部为整数")
        if self.H < self.L:
            raise ValueError(f"零件高度 H (当前为{self.H}) 不允许小于长度 L (当前为{self.L})")
        if self.L % 2 != 0:
            raise ValueError("零件尺寸 L 必须为偶数")
        if self.H % 2 != 0:
            raise ValueError("零件尺寸 H 必须为偶数")
        max = sorted([self.L, 2*self.W, self.H])[-1]
        max_2 = sorted([self.L, 2*self.W, self.H])[-2]
        diff = max - max_2
        if diff < 2:
            raise ValueError(f"零件尺寸最大的(当前为{max})与次大的(当前为{max_2})之间相差不足 2 个单位")
        elif diff > 2:
            raise ValueError(f"零件尺寸最大的(当前为{max})与次大的(当前为{max_2})之间相差超过 2 个单位")

if __name__ == "__main__":
    L = 2
    W = 2
    H = 6
    generator = Part(L, W, H)
    generator.validate_dimensions()