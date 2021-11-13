print("hello world!")


avariable = ""
a_variable = ""
_a_varaible_ = ""
aVaraible = ""
AVARAIBLE = ""
avariable2 = ""

x , y , z = "test1" , "test2", "test3"

print (x)
print (y)
print (z)


#outputting variables

print("Python "+ x)

a = x + y
print(a)

#declared globally and can be accessed inside functions
x = "hello world"

def afunction():
    print("things "+ x)

afunction()



def afunction2():
    global x
    x = "hello world 2"

afunction2()

print("print something" + x)