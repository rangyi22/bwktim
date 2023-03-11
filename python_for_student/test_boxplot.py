#test_boxplot.py
import numpy as np
g = [65,67,68,68,68,69,69,69,69,70,70,70,70,70,71,71,71,71.5,74]
Q1,Q3,Q2 = np.percentile(g,[25,75,50]) # 1st/3rd quartiles, Median
IQR = Q3 - Q1  # Interquartile range
k = 1.5
Lower_fence = Q1 - k*IQR; Upper_fence = Q3 + k*IQR 
outside = lambda x: x<Lower_fence or x>Upper_fence
inside = lambda x: Lower_fence<=x<=Upper_fence # not outside
g_ = list(filter(inside, g))
outliers = list(filter(outside, g))
Lower_whisker = min(g_);  Upper_whisker = max(g_)
print(f'Outliers = {outliers}')
print(f'Lower_whisker = {Lower_whisker}, Q1={Q1}, Q2={Q2}, Q3={Q3}, Upper_whisker={Upper_whisker}')
