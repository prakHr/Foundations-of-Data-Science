from typing import Any, Union

import numpy as np
from numpy.core.multiarray import ndarray
from scipy.special import gamma as Y
from scipy.misc import comb as C
import matplotlib.pyplot as plt

# 1 for heads 0 for tails
N = 150
data = np.random.choice([0, 1], size=N)

posterior = {'a': 1, 'b': 1}


def run_sequential(n):
    for i in range(n):
        if data[i] == 0:
            posterior['b'] += 1
        else:
            posterior['a'] += 1
        # plot
        a = posterior['a']
        b = posterior['b']
        x = np.linspace(0, 1, 1000)
        y = (Y(a + b) / Y(a) * Y(b)) * (x ** (a - 1)) * ((1 - x) ** (b - 1))
        plt.figure(figsize=(15, 15))
        plt.plot(x, y)
        plt.title("Gamma Distribution params a:{} b:{}.Samples:{}".format(a, b, i + 1))
        plt.savefig("distribution_for_samples_{}".format(i + 1) + str(".png"))
        plt.close()


run_sequential(N)


def run_once(n):
    m = np.sum(data)
    l = n - m  # type: int
    return C(n, m) * (0.5 ** m) * (0.5 ** l)


print(" Result:", run_once(N))
