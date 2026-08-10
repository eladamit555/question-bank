#start
Y = int(input('fuel: '))
X = int(input('count down from: '))
while X  > 0:
    Y = Y - X * 2.5
    if Y < 0:
        print('out of fuel at T minus', X)
        break
    print('T minus', X, '|', 'left fuel', Y)
    X = X - 1
if Y > 0:
    print('lift off! fuel left:', Y)
#stop
