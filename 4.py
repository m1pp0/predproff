'''Считываем csv файл'''
import csv
with open('products.csv', 'r', encoding='cp1251') as file:
    data = list(csv.DictReader(file, delimiter=';'))

'''Создаём временный csv файл с новым столбцом "promocode"'''
with open('products4.csv', 'w', encoding='cp1251') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count', 'promocode'])
    writer.writeheader()
    writer.writerows(data)

'''Считываем новый csv файл'''
with open('products4.csv', 'r', encoding='cp1251') as file:
    data2 = list(csv.DictReader(file, delimiter=';'))

for i in data2:
    i['promocode'] = i['product'][:2] + i['Date'][:2] + i['product'][-2:][::-1] + i['Date'][3:5][::-1]
    '''Проходимся по списку словарей, добавляя сгенерированный промокод в каждый из них'''

'''Сохраняем изменения в новый файл'''
with open('product_promo.csv', 'w', encoding='cp1251') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count', 'promocode'])
    writer.writeheader()
    writer.writerows(data)
