import random as r
age=r.randint(1,10)

print(age)
flag = False

def main_game(n,secretage):
    if n != secretage:
        return 'incorrect'

    elif n==secretage:
        return 'correct'


for i in range(1,6):
    print('You have ' + str(6-i)+ ' gusses. '+'Guess the age-')
    n=int(input())
    if main_game(n,age) == 'correct':
        print('You Won!!!!!!!!!')
        flag = True
        break

if not flag:
    print('You Loooooossssssseeeee')


#print(type(n))
#print(type(age))
