import numpy as np

class SixPieceBurrPuzzle:
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
        self.max_dim = max(self.L, self.W, self.H)
        self.whole_space = np.zeros((self.max_dim, self.max_dim, self.max_dim), dtype=int)
    # 求重合区域
    
    # 遍历构建零件