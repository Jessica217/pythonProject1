import numpy as np
import matplotlib.pyplot as plt
from skimage import io

# 路径可能需要根据你的文件存放位置进行调整
blank_image_path = 'DATA/blank.tif'

# 读取空白图像文件
blank_image = io.imread(blank_image_path).astype(np.float32)

# 确定阳极和阴极在图像中的位置（这需要实验或文档中的额外信息）
# 例如，我们假设阳极在左侧，阴极在右侧，且我们感兴趣的是垂直中心线
# 注意：具体的索引取决于图像的方向和坐标系
y_position = blank_image.shape[0] // 2  # 中心线
intensity_profile = blank_image[y_position, :]

# 绘制强度轮廓图
plt.figure(figsize=(10, 4))
plt.plot(intensity_profile, label='Intensity Profile')

# 假设图像的左侧是阴极，右侧是阳极
plt.text(0, max(intensity_profile), 'Cathode', ha='center', va='bottom')
plt.text(len(intensity_profile)-1, max(intensity_profile), 'Anode', ha='center', va='bottom')

plt.xlabel('Pixel Position')
plt.ylabel('Intensity')
plt.title('Line Intensity Profile from Cathode to Anode')
plt.legend()
plt.show()
