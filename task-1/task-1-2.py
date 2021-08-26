digits = 0
temp = 0
summ = 0
summfull = 0
a = []
i = 0
for i in range(1, 100):
    if i % 2 != 0:
        temp = i ** 3
        a.append(temp)
        while temp > 0:
            digits = temp % 10
            summ = summ + digits
            temp = temp // 10
        if summ % 7 == 0:
            summfull = summfull + (i ** 3)
            print (summ, i ** 3)
        summ = 0
print ('summfull: ', summfull)
i = 0
summseventeen = 0
summfinal = 0
while i < len(a):
    print(a[i], ' index: ', i)
    summseventeen = a[i] + 17
    digits = 0
    while summseventeen > 0:
        digits = digits + (summseventeen % 10)
        summseventeen = summseventeen // 10
    if digits % 7 == 0:
        summfinal = summfinal + a[i] + 17
    i = i + 1
print ('summfinal: ', summfinal)
