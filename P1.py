'''In second year computer engineering class, group A student’s play cricket, group B
students play badminton and group C students play football.
Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET
built-in functions)'''


cricket=[' ','a','b','c']
badminton=[' ','b','d','e']
football=[' ','a','b','e','f']
l1=[]
l2=[]

while True:
    name=input("Enter Player's Name \n")
    if name=="":
        break
    game=input("Enter Game You Play\n")
    game=game.lower()
    # print(game)
    if game=='cricket':
        for i in cricket:
            if i==name:
                break
        if i==name:
            continue
        cricket.append(name)
    elif game=='football':
        for i in football:
            if i==name:
                break
        if i==name:
            continue
        football.append(name)
    elif game=='badminton':
        for i in badminton:
            if i==name:
                break
        if i==name:
            continue
        badminton.append(name)

# Q1  List of students who play both cricket and badminton

print("List of students who play both cricket and badminton :")
for i in cricket:
    for j in badminton:
        if i==j:
            print(i)
            l1.append(i)
print('\n')

# Q2  List of students who play either cricket or badminton but not both

print("List of students who play either cricket or badminton but not both :")
for i in cricket:
    for j in badminton:
        if i==j:
            break
    if i==j:
        continue
    print(i)
    l1.append(i)
for i in badminton:
    for j in cricket:
        if i==j:
            break
    if i==j:
        continue
    print(i)
    l1.append(i)
print('\n')

# Q3  Number of students who play neither cricket nor badminton

print("Number of students who play neither cricket nor badminton. :",end=' ')
y=0
for i in football:
    for j in l1:
        if i==j:
            break
    if i==j:
        continue
    y+=1
print(y)
print('\n')

    # print(i)


# @4  Number of students who play cricket and football but not badminton.

print("Number of students who play cricket and football but not badminton. :",end=' ')
x=0
for i in football:
    l2.append(i)
for i in cricket:
    for j in football:
        if i==j:
            break
    if i==j:
        continue
    l2.append(i)

for i in l2:
    for j in badminton:
        if i==j:
            break
    if i==j:
        continue
    x+=1
print(x)
        

        
