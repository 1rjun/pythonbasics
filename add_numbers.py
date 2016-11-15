__author__ = 'Arjun Singh'
#this will write the output of sum of programs in the file
def add(*args): #take the any number of amount of arguments
    total=0
    for i in args:
        total=total+i
    return total

first=add(1,2,10,3,2) #store the add function return value result in first variable
ad=[1,2,3,4,2]  # ad is a list
second=add(*ad)# unpacked argument value passed to function add
print(first)
print(second)
writefile=open('add_numbers.out','w')
writefile.write(str(first))
writefile.write('\n'+str(second))
writefile.close()


