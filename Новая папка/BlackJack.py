koloda = [6,7,8,9,10,2,3,4,11] * 4
import random
random.shuffle(koloda)
print('Поиграем в очечко?')
count = 0

while True:
    choice = input('Бери карту, браток? y/n\n')
    if choice == 'y':
        current = koloda.pop()
        print('Ты вытянул %d' %current)
        count += current
        if count > 21:
            print('Сорян, ты продул')
            break
        elif count == 21:
            print('Поздравляю, у тебя ОЧКО!')
            break
        else:
            print('У тебя %d очков.' %count)
    elif choice == 'n':
        print('У тебя %d очков и ты закончил игру.' %count)
        break

print('Бывай!')