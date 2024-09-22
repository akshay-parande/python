'''Write a Python program to store marks scored in subject “Fundamental of Data
Structure” by N students in the class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
?.... d) Display mark with highest frequency'''


class frc:
    def __init__(self,F):
        self.F=F

T_m=0
H_s=0
L_s=100
Abs_S=0
H_f={}
frc=0
n=int(input("Enter no of Student : "))
l1=[]
for i in range(1,n+1):
    name=input("Name of student : ")
    mark=input("Marks of student")
    if mark.isdigit():
        H_f[mark]=frc
        mark=int(mark)     
        T_m=T_m+mark
        l1.append(mark)
        if H_s<mark:
            H_s=mark
        if L_s>mark:
            L_s=mark
    else:
        Abs_S+=1
    
    # name=FDS_S(mark)



# Q1  The average score of class

print("The average score of class is :",end=' ')
avg=T_m/n
print(avg)

# Q2  Highest score and lowest score of class

print(f"Highest score of the class is : {H_s} and Lowest score of class is : {L_s}")

# Q3  Count of students who were absent for the test

print(f"Count of students who were absent for the test is : {Abs_S}")

# Q4  Display mark with highest frequency

print("Mark with highest frequency is ")

