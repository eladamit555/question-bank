#start
orders = int(input('how many orders'))
total_slices = 0
if orders == 0:
    print('no pizza tonight')
for i in range(1, orders + 1):
    slices = int(input('how many slices'))
    friends = int(input('how many friends'))
    x = slices // friends
    print('each friend get', x, 'slices')
    if slices % friends == 0:
        print('perfect split')
        total_slices += slices
    else:
        print('leftover for the dog', slices % friends)
        total_slices += slices
    print('total slices:', total_slices)
    print('average slices:', total_slices / orders)
#stop








