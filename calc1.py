import sys, numbers
import math, cmath , logging


fileHandle = open ( 'log2.txt',"r")
lastnumber = fileHandle.read()
print("Previous output of the program is ----" +lastnumber)
def func(num):
    try:
        a=num
        if a[0]=='+':
            solution= eval (lastnumber+a)


        elif a[0]=='-':
             solution= eval (lastnumber+a)

        elif a[0]=='*':
            number=int(a[1:])
            lastnumberx=int (lastnumber)
            solution= lastnumberx*number
        elif a[0]=='/':
            number=int (a[1:])
            lastnumberx = int (l+lastnumber)
            solution = lastnumberx / number

        else:
            solution=eval(a)

        return solution
    except SyntaxError:
        return "No expression after the the given number"
    except TypeError:
        return "Cannot add a symbol or letter"
    except ZeroDivisionError:
        return "cant divide with 0!!!!"
    except IndexError:
        return "No expression entered, Please enter something!!!!"

    except NameError:
        l= a[4:-1]

    except ValueError:
        return "enter valid string"

    if a[0]=='s':
        return math.sin(float(l))
    elif a[0]=='c':
        return math.cos(float(l))

    elif a[0]=='t':
        return math.tan(float(l))
    elif a[0]=='l':
        return math.log(float(l),10)

k=func(sys.argv[1])




# nextinput=0
# nextinput = str(input("do you wanna input any more number to the above solution"))

# l=func(str(input("enter another number")))


# while True:
#
#      nextinput = str(input("do you wanna input any more number to the above solution"))
#      l= eval( lastnumber + nextinput)
#      print(l)

f2=open("log2.txt","w")
f2.write(str(k))
logging.basicConfig(filename="logmain.txt",format='%(asctime)s %(message)s',filemode='a+')
logger1 = logging.getLogger()
logger1.setLevel(logging.DEBUG)
handler=logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter1=logging.Formatter('%(asctime)s-%(message)s')
handler.setFormatter(formatter1)
logger1.addHandler(handler)
logger1.info('This is our input ||||||||||:-------'+ sys.argv[1] +' ||||||||||      This is our output:-------' +str(k))



while True:
    inp = str(input())

    if inp[0]=='*':
        inp1=int(inp[1:])
        k= k*inp1
        print(k)
    else:

        k=k+int(inp)
        print(k)