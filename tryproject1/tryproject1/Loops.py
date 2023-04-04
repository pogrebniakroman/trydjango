total_summa = 0
for i in range(5):
    price = float(input('Input price of good: '))
    quantity = float(input('Input quantity: '))
    current_summa = price * quantity
    total_summa = current_summa + total_summa
    print('Summarization: ', total_summa)