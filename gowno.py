import numpy as np
import scipy.stats as stats

alpha = 0.975
max_k = 50


def get_difference(k):
    normalny = stats.norm.ppf(alpha)
    t = stats.t.ppf(alpha, k)
    print(f"k rzędu {k} i norm {normalny} - t student{t}")
    return abs(normalny - t)


i = 1
while i < max_k:
    if get_difference(i) < 0.01:
        print(i)
        break
    i += 1
