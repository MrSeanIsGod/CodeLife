import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 使用微软雅黑字体
plt.rcParams['axes.unicode_minus'] = False

# 绘制示例图
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('示例图')
plt.xlabel('X 轴')
plt.ylabel('Y 轴')
plt.show()