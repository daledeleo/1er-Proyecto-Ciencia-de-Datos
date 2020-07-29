import pandas as np

df=np.read_csv('./datos/espol-DeliveriesData.csv',encoding='latin-1',error_bad_lines=False)
print(df.head())