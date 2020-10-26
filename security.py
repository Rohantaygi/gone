class friends:
    __leaves = 10                           #private var
    _money = 20                             #protected var
    guns = 30                               #public var
    def __init__(self, aname, arole):
        self.name = aname
        self.role = arole

har = friends("Harry", "programmer")
#usage-

print(har._money)
print(har._friends__leaves)
print(har.guns)
