import time

words = {"abundant":"to remain closed", "psychology":"study of mentally disabled people",
"reticence":"a person who is not in a mood to talk", "time":"the most precious thing in earth"}

print('words to search are-\n reticence\n psychology\n time\n abundant\n')

while True:
    a = input('enter a word: ')
    b = words.get(a)
    print(b)

    print(' ')
    
    if a == 'exit':
        break

print('good bye')
time.sleep(2)
