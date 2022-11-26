salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

i = 0 # счетчик месяцев
while i <= months-1:
    money_capital += spend - salary # разница между тратами и зарплатой
    spend *= 1.03 # увеличение расходов из-за роста цен
    i += 1 # счетчик (шаг цикла)

print(round(money_capital))
