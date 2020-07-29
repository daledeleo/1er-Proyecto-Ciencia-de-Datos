import pandas as np

df=np.read_csv('./datos/espol-DeliveriesData.csv',error_bad_lines=False)
print(df.head())
