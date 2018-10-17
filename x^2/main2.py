import random
import numpy as np

# 产生五个随机中心
# 产生一个随机中心
def kmp_firstCenter(pixelCount):
    return random.randint(0,pixelCount)

# 两点距离
def distance(x,y):
    return np.sqrt(np.sum(np.square(x-y)))

# 最小距离
def min_distance(x,centers):
    temp_dis = distance(x,centers[0])
    ret = temp_dis
    for ele in centers:
        temp_dis = distance(x,ele)
        if ret > temp_dis:
            ret = temp_dis
    return ret

# 产生 其他随机点
def kmp_otherCenter(centers,coors):
    # 计算所有点与已知中心的最近的距离,求和
    dis_sum = 0
    for x in coors:
        dis_sum += min_distance(x,centers)
    # 产生随机值
    rx = np.random.uniform() * dis_sum
    # 选取中心点
    for x in coors:
        rx -= min_distance(x)
        if  rx <= 0:
            return x
# 计算各区域的中心
# 更新5个区域
# 更新5个中心,如果5个中心不变,就结束

