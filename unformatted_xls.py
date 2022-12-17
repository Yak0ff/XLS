import pandas as pd
merger = pd.DataFrame()
file = 'Мониторинг ТОиТР 2022 update.xlsx'

df = pd.read_excel(file, sheet_name='Sheet1')
filt = pd.read_excel(file, sheet_name='Лист1')

merger = merger.append(filt, ignore_index=True)
merger = merger.append(df,ignore_index=True)
merger.to_excel('merged.xlsx')
