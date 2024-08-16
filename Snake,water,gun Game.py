import random

print()
print('Welcome To Our Game "Snake, Water & Gun"')
print('You have 5 chance.')
print('>s for snake\n>w for water\n>g for gun')
print()

com_point = 0
your_point = 0

i = 1
while i <= 10:
    com_op = random.choice(['snake', 'water', 'gun'])
    user_op = input('You choose [snake:water:gun]:')
    print('Computer choose:', com_op)

    if user_op.lower() == 's' and com_op == 'water':
        print('You won 1 point. ')
        your_point = your_point+1

    elif user_op.lower() == 'w' and com_op == 'gun':
        print('You won 1 point. ')
        your_point = your_point+1

    elif user_op.lower() == 'g' and com_op == 'snake':
        print('You won 1 point. ')
        your_point = your_point+1

    elif user_op.lower() == 's' and com_op == 'gun':
        print('Computer won 1 point. ')
        com_point = com_point+1

    elif user_op.lower() == 'w' and com_op == 'snake':
        print('Computer won 1 point. ')
        com_point = com_point+1

    elif user_op.lower() == 'g' and com_op == 'water':
        print('Computer won 1 point. ')
        com_point = com_point + 1

    elif user_op.lower() == 's' and com_op == 'snake':
        print('Tie, No one will get any point. ')

    elif user_op.lower() == 'w' and com_op == 'water':
        print('Tie, No one will get any point. ')

    elif user_op.lower() == 'g' and com_op == 'gun':
        print('Tie, No one will get any point. ')

    else:
        print('''You loosed one chance,Be careful.''')

    i = i+1

print()
print('~~ Game Over ~~')

if your_point > com_point:
    print('''Congratulation,You win this match.''')

elif your_point < com_point:
    print('Computer win this match.')

else:
    print('Match Tie')

print(f"Your point = {your_point}")
print(f"computer point = {com_point}")