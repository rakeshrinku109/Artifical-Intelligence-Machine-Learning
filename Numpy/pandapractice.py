import numpy as np
import pandas as pd



price_list = [100, 200, 300, 400, 500]
med_price_array  =  np.array(price_list)
series_list = pd.Series(price_list)
series_list2 = pd.Series(med_price_array)   
print(series_list)
print(series_list2)

