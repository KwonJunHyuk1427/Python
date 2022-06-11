#Local Variable
def func1():
    num = 1
    print(num)
func1()

#Global Variable
num = 10
def func2():
    global num
    num += 1
    print(num)
func2()

#Writing Mode
f = open("test.txt", "w")
f.write("Hi")
f.close()

#Append Mode
f = open("test.txt", "a")
f.write("World")
f.close()

#Reading Mode
f = open("test.txt", "r")
result = f.readlines()
f.close()
print(result)