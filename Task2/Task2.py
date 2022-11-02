def triangle(a):
    i = 1
    while i <= a+1:
        print(' ' * (a + 1 - i) + '*' * (2 * i - 1) + ' ' * (a + 1 - i))
        i += 1
try:
    a = int(input())
except:
    print('Enter right numbers')
triangle(a)