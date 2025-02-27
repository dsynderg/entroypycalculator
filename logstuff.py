import math
list_of_stuff=[]
sum=0
def make_I_a_fration(i):
    fration = i.split("/")
    return (float(fration[0])/float(fration[1]))

while True:
    user_input = input("enter a number: ")
    if user_input == "":
        for i in list_of_stuff:
            i= make_I_a_fration(i)
            sum -= (i)*math.log(float(i),2)
        print(sum)
        sum = 0
        list_of_stuff=[]
    else:
        if user_input == "end":
            break
        list_of_stuff.append(user_input)