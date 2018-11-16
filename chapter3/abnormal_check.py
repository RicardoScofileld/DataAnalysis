# coding=utf-8
import pandas as pd
import matplotlib.pylab as plt


catering_sale = '../resource/catering_sale.xls'  # 餐饮数据路径
data = pd.read_excel(catering_sale, index_col='日期')  # 读取数据

plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 正常显示符号

plt.figure()  # 建立图像
p = data.boxplot(return_type='dict')  # 箱型图
x = p['fliers'][0].get_xdata()  # flies为异常值的标签
y = p['fliers'][0].get_ydata()  # 
y.sort()

for i in range(len(x)):
	if i > 0:
		plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i]+0.05 - 0.8/(y[i]-y[i-1]), y[i]))
	else:
		plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i]+0.08, y[i]))
plt.show()