glist = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
s = ''
i = 0

print(len(glist))

while i < len(glist):
    s = glist[i]
    if s.isdigit():
        glist[i] = str(f'{int(glist[i]):02}')
        glist.insert(i,'"')
        glist.insert(i+2, '"')
        i = i + 2
    i = i + 1
print(glist)

#print('5'.isdigit())

#print('+849'.isdigit())
#print('+849'.isalnum())
#print('+849'.isdecimal())
#print('+849'.isnumeric())