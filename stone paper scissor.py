import random
import time

print('             stone, paper, scissor')

print(' ')

lives = 10
score = 0

functions = ["Stone", "Paper", "Scissor"]

while not (lives == 0):
    pc = random.choice(functions)
    user_inp = input('your choice: ')
    if pc == 'Stone' and user_inp == 'paper':
        print('AI choosen: ', (pc))
        print('you won')
        score += 1 
        print('lives remaining:', (lives))
        print(' ')
    elif pc == 'Paper' and user_inp == 'scissor':
        print('AI choosen: ', (pc))
        print('you won')
        score += 1 
        print('lives remaining:', (lives))
        print(' ')
    elif pc == 'Scissor' and user_inp == 'stone':
        print('AI choosen: ', (pc))
        print('you won')
        score += 1 
        print('lives remaining:', (lives))
        print(' ')
    elif pc == user_inp:
        print('tie')
        print(' ')
    else:
        print('you lost') 
        print('AI choosen: ', (pc))
        lives -= 1
        print('remaining lives: ', (lives))
        print(' ')
    
print('your final score is', (score))
print('you played well')

time.sleep(2)
