import pandas as pd


# Read sheet with numbers from xls book
inv_numb = pd.read_excel('Мониторинг ТОиТР 2022 update.xlsx', sheet_name='Лист1')

just_inv = inv_numb.values
#print (just_inv.pop(0))
#print(book)