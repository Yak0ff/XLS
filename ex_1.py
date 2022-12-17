# часть первая
import pandas as pd

files = ['january.xlsx',
         'february.xlsx',
         'march.xlsx']
merger = pd.DataFrame()  # часть вторая
for file in files:
    df = pd.read_excel(file, skiprows=3)
    merger = merger.append(df, ignore_index=True)

# сохраняем
merger.to_excel('merger.xlsx')