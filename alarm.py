import pandas as pd
import matplotlib.pyplot as plt


def ss_choice(choice_array):  # Функция выбора из таблицы. Параметр - что выбираем
    return alarm[choice_array].unique()


alarm = pd.read_excel('alarm.xlsx', header=1)  # Открываем экспортированный из учета отказов файл xlsx /Имя другое/

ss = ss_choice("Служба связи")  # Здесь будет результат функции выбора по службам. Нужна уникальная выборка
ss = ss[5]  # Сосногорский цех ТС
sistema_s = ss_choice("Система связи")  # Здесь будет результат функции выбора по системам связи. Нужна уникальная выборка

sts = alarm[alarm["Служба связи"] == ss]  # выбираем все записи по службе связи
fail = sts[sts["Текущее состояние"] == "Не устранено"]  # Находим не устраненные
rec_total = alarm["№ п/п"].count()  # Сосчитаем сколько всего записей. Вместо max() используем для будущей функции
ss_total = sts["№ п/п"].count()  # Сколько записей по цеху

# print(sts)
# print(sistema_s[2:13])
# print(ss)
print("Всего по службе связи "+ss+": "+str(ss_total)+" повреждений ("+ str(round((ss_total/rec_total)*100))+"%). Из них не устранено "+str(fail["№ п/п"].count()))
# alarm.plot().imshow


