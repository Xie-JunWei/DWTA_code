import numpy as np
import math

# 敌我兵力数量配置
num_of_target = 10
num_of_weapon = 15

# 仿真时间总长
all_time = 10000

# time slot长度
slot = 2

# 目标类型特征
target_attribute = {0: [], 1: [], 2: [], 3: []}
# 拦截弹类型特征
Interceptor_attribute = {0: [], 1: [], 2: [], 3: []}

# 作战场景初始化

