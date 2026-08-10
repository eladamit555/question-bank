#start
hottest = None
coldest = None
while True:
    temp = input('temp?')
    if temp == 'done':
        break
    temp = float(temp)
    if temp >= 30:
        print('heatwave')
    if 15 < temp < 30:
        print('nice')
    if 0 < temp <= 15:
        print('chily')
    if temp < 0:
        print('freezing')
    if hottest is None or temp > hottest:
        hottest = temp
    if coldest is None or temp < coldest:
        coldest = temp
if hottest is None and coldest is None:
    print('no measurements')
else:
    spread = hottest - coldest
    print('hottest:', hottest)
    print('coldest:', coldest)
    print('spread:', spread)
