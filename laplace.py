# Created by jikangwang at 4/25/19

import matplotlib.pyplot as plt
import numpy as np


def noisyCount(sensitivety, epsilon):
    beta = sensitivety / epsilon
    u1 = np.random.random()
    u2 = np.random.random()
    if u1 <= 0.5:
        n_value = -beta * np.log(1. - u2)
    else:
        n_value = beta * np.log(u2)
    #print(n_value)
    return n_value/100


def laplace_mech(data, sensitivety, epsilon):
    for i in range(len(data)):
        data[i] += noisyCount(sensitivety, epsilon)
    return data


if __name__ == '__main__':
    x = [0.83,0.12,0.36]
    my_new_list = [i * 100 for i in x]
    sensitivety = 1
    epsilon = 1
    data = laplace_mech(x, sensitivety, epsilon)
    for j in data:
        print(j)