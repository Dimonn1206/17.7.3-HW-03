per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a = per_cent
money = int(input("Введите сумму:"))
b = money

deposit = a.get('ТКБ')*b/100, a.get('СКБ')*b/100, a.get('ВТБ')*b/100, a.get('СБЕР')*b/100

print(list(map(int, deposit)))

max_deposit = max(list(map(int, deposit)))
print("Максимальная сумма, которую вы можете заработать:", max_deposit)