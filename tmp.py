
for x in range(1590,900,-20):
    print('%4d'%x,end=' ')
print()
for a in range(1590,900,-20):
    print(a)
    for x in range(1590,900,-20):
        if a <= x:
            tmp=21-15*x/a
            if tmp>=0:
                print('%.2f'%(tmp), end=' ')
            else:
                print('   0',end=' ')
        else:
            tmp=18.67-12.67*x/a
            if tmp < 8:
                print('%.2f'%(tmp), end=' ')
            else:
                print('   8',end=' ')
    print()
