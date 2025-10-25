import numpy as np

# 读取原始数据
data = np.loadtxt(r'D:\part1\progress_data\subsample\point_density5_cylinder\5\ground.txt')

# 提取相关列
y = data[:, 1]
z = data[:, 2]
angle_deg = data[:, 7] # 第8列（角度）
col9 = data[:, 8]
new_column = np.sqrt((15 - y) ** 2 + (500 - z) ** 2)
angle_rad = np.radians(angle_deg)         # 转换为弧度
cos_angle = np.cos(angle_rad)
result = (new_column ** 2 / 500**2) / cos_angle
final_value = col9 * result
final_data = np.column_stack((data, new_column, result, final_value))
np.savetxt(r'D:\part1\progress_data\subsample\point_density5_cylinder\5\ground_correction_progress.txt', final_data, fmt='%.6f')
# 提取前8列和最后一列（第12列）
correction_data = np.column_stack((data[:, :8], final_value))
# 保存为 correction_ground_final.txt
np.savetxt(r'D:\part1\progress_data\subsample\point_density5_cylinder\5\ground_correction_final.txt', correction_data, fmt='%.6f')
