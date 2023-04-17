INÍCIO = int(input())
FIM = int(input())
primo = 0

for i in range(INÍCIO, FIM+1):
    if i > 1:
        for x in range(2, i):
            if(i % x == 0):
                break
        else:
            print(i, ',', end='')
            primo += 1

print(f'primos: {primo}')