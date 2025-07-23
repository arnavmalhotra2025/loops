#activity 1
#input an integer value
n = int(input("enter the number whose sum you want to find: "))
sum = 0

for i in range(1 , n+1):
    sum = sum+i
    print("\n Sum =", sum)

#activity 2
string = input ("please enter your own string:")

string2 = ('')
for i in string:
    string2 = i + string2
    
print("\n the original string=", string)
print("the reversed string =", string2)

#activity 3
n = int(input("enter thee value of n : "))

print("numbers from {0} to {1} are:".format(n,1))

for i in range(n,0,-1):
    print(i)
    