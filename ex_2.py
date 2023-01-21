import pandas as pd


# Read sheet with numbers from xls book
inv_numb = pd.read_excel('Мониторинг ТОиТР 2022 update.xlsx', sheet_name='Лист1')
work_sheet = pd.read_excel('Мониторинг ТОиТР 2022 update.xlsx', sheet_name='Sheet1')
just_inv = inv_numb ["Инв. номер"] #Теперь можно получать значения для фильтра обратившись just_inv[индекс]
to_new = pd.merge(work_sheet, inv_numb, how="left", on="Инв. номер")
merged = pd.DataFrame()
merged = merged.append(to_new, ignore_index=False)
merged.to_excel("merged.xlsx")
print((to_new.head()))
"""
for i in range(len(just_inv)):
    to_filt = work_sheet[work_sheet["Инв. номер"].isin(just_inv[i])]
print(to_filt)
"""
"""
count = 1
print(type (len(just_inv)), ':', type(count))
for i in range(len(just_inv)):
    #print (just_inv[i] + '--' + work_sheet["Инв. номер"])
    #print(just_inv[i])
    #print(work_sheet["Инв. номер"][i])
    if just_inv[i] == work_sheet["Инв. номер"][i]:
        count += 1
        print ("Совпало")
        print(str(just_inv[i]) + '--' + str(work_sheet["Инв. номер"][i]))
print(count, ' i=', i)
"""
#print(just_inv)
#print (type (just_inv))
#print (just_inv.pop(0))
#print(book)