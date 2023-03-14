import pandas as pd
import matplotlib.pyplot as plt

alarm = pd.read_excel('alarm.xlsx',header=1) #Открываем экспортированный из учета отказов файл xlsx /Имя другое/
scts = alarm[alarm["Служба связи"] == "Сосногорский цех ТС"] # выбираем все записи по СЦТС
fail = scts[scts["Текущее состояние"] == "Не устранено"] #Находим не устраненные
rec_total = alarm["№ п/п"].count() #Сосчитаем сколько всего записей. Вместо max() используем для будущей функции
ss_total = scts["№ п/п"].count() #Сколько записей по цеху
alarm.plot()


