
#i am learning from tutorial number 45
lis = ["Bhindi", "Aloo", "Chopsticks", "Gaajar", "Lollypop"]

#enumerate function(helps in printing the specific item in list)-
for index, item in enumerate(lis):
    if index%2 == 0:
        print(f'jarvis please buy {item}')

#how args*/kwargs** works(now we can add any name in the git var and it will be printed in the function)-
def beast(*args):
    print(str(args))
    print(type(args))

git = ["Rohan", "Harry", "Praganya", "Kinshuk"]
beast(*git)

def github(a, b):
#git hub.com(function)-
    print(a + b - 1)

github(4, 4)

#if __name__ == __main__ (necessary):
if __name__ == "__main__":
    def rohan(string):
        return "give this to me"

    def add(a, b):
        return a + b - 5

    print(add(2, 5))

#map(usage):
numbers = ["3", "5", "65"]
numbers = list(map(int, numbers))

numbers[2] = numbers[2] + 1
print(numbers[2])

#OOPS-
class rohan:
    pass

Praganya = rohan()

Praganya.name = "Praganya"
Praganya.std = 7
Praganya.age = 12
Praganya.sbj = ["Science", "History"]

print(Praganya.sbj)

#returners-
def function(g):
    if g == 0:
        return ('0')
    if g > 0:
        return ('more than 0')

call = function(0)
print(call)

#decoraters-
def rb(func1):
    def nowexec():
        print('executing now')
        func1()
        print('executed')
    return nowexec

@rb
def who_am_i():
    print('a good boy')

who_am_i()

#abstraction- tukdo me baatna
#encapsulation- un tukdo ko combine karna aur abstraction ki details ko hide kr dena

#polymorphism-
print(1 + 2)
print("1" + "2")

