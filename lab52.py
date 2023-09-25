
# Online Python - IDE, Editor, Compiler, Interpreter
N = int(input("Enter the positive number: "))
if N <= 0:
    print("enter the positive number : ")
else:
    i = 1
    while i <= 1000:
        if i % N == 0:
            i+=1
            continue
        print(i)
        i+=1

