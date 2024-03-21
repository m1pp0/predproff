import csv
'''Считываем csv файл'''
with open('products.csv', 'r', encoding='cp1251') as file:
    data = list(csv.DictReader(file, delimiter=';'))
summ_zakus = 0
'''Создаём новый файл с новым столбцом "total"'''
with open('products2.csv', 'w', encoding='cp1251') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count', 'total'])
    writer.writeheader()
    writer.writerows(data)
'''Считываем новый файл, создаём список словарей'''
with open('products2.csv', 'r', encoding='cp1251') as file:
    data2 = list(csv.DictReader(file, delimiter=';'))
'''Проходимся по списку, добавляя значения в i[total], а также образуя сумму по категории "Закуски"'''
for i in data2:
    i['total'] = int(i['Count'][:-2])*int(i['Price per unit'][:-2])
    if i['Category'] == 'Закуски': summ_zakus += int(i['total'])

'''Выводим нужную сумму'''
print(summ_zakus)
'''Сохраняем обновлённые данные в новый файл'''
with open('products_new.csv', 'w', encoding='cp1251') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count', 'total'])
    writer.writeheader()
    writer.writerows(data2)
