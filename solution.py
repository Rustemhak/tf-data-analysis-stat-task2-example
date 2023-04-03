import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 326525586 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    scale_estimate = np.sum(x**2) / len(x) / 22
    lower_quantile = chi2.ppf(alpha / 2, df=2 * len(x))
    upper_quantile = chi2.ppf(1 - alpha / 2, df=2 * len(x))
    lower_bound_sigma = np.sqrt((len(x) * scale_estimate) / upper_quantile)
    upper_bound_sigma = np.sqrt((len(x) * scale_estimate) / lower_quantile)
    return lower_bound_sigma, upper_bound_sigma
