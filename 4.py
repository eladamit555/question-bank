snack = int(input('[snack 1, 2, 3:]'))
while True:
    if snack == 1:
        price = 7
        break
    elif snack == 2:
        price = 5
        break
    elif snack == 3:
        price = 3
        break
    else:
        print('unknown code, try again')
        snack = int(input('[snack 1, 2, 3:]'))
paid = 0
pieces = 0
biggest = None

while paid < price:
    money = int(input('insert your money: '))

    if money != 1 and money != 5 and money != 10 and money != 20 and money != 50:
        print('the machine spits it out')
    else:
        paid += money
        pieces += 1
        if biggest == None or money > biggest:
            biggest = money
change = paid - price
if change == 0:
    print('no change, exact!')
else:
    print('change:',  change)

print('biggest:', biggest)
print('money accepted:', pieces)
avg = paid / pieces
print('avg:', avg)
#stop






