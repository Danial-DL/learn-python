li = []
def Num():
    for i in range(5):
        li.append(i)
    return li
list1 = Num()
def plus_num(list_2):
    a = 0
    for i in list_2:
        a += i
    print(a)
plus_num(list1)
