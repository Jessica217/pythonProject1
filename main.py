import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from skimage import io

# 路径可能需要根据你的文件存放位置进行调整
raw_image_path = 'DATA/1.tif'
blank_image_path = 'DATA/blank.tif'
dark_image_path = 'DATA/dark.tif'

# 读取图像文件
raw_image = io.imread(raw_image_path).astype(np.float32)
blank_image = io.imread(blank_image_path).astype(np.float32)
dark_image = io.imread(dark_image_path).astype(np.float32)

# 步骤1: 减去暗场图像
corrected_image = raw_image - dark_image

# 步骤2: 标准化
# 注意避免除以零
normalized_image = np.where(blank_image - dark_image != 0, corrected_image / (blank_image - dark_image), 0)

# 步骤3: 对比度增强
# 使用matplotlib的imshow进行对比度增强显示
plt.imshow(normalized_image, cmap=cm.gray)
plt.colorbar()
plt.show()

