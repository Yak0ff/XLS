import pandas as pd

# Read sheet with numbers from xls book
inv_numb = pd.read_excel('Мониторинг ТОиТР 2022 update.xlsx', sheet_name='Лист1')
work_sheet = pd.read_excel('Мониторинг ТОиТР 2022 update.xlsx', sheet_name='Sheet1')
just_inv = inv_numb ["Инв. номер"] #Теперь можно получать значения для фильтра обратившись just_inv[индекс]
#print(just_inv.values)
list_just_inv = just_inv.to_list()
# print(list_just_inv)
for count in range(len(list_just_inv)):
    mynum = list_just_inv[count]
    print(f'На оборудование {mynum} установить ПО')
"""
to_new = pd.merge(work_sheet, inv_numb, how="left", on="Инв. номер")
merged = pd.DataFrame()
merged = merged.append(to_new, ignore_index=False)
merged.to_excel("merged.xlsx")
print(to_new.head())
"""