
import sys, numbers
import math, cmath , logging


fileHandle = open (sys.argv[1],"r")
lastnumber = fileHandle.read()




print("Previous output of the program is ----" +lastnumber)

def func(num):
    try:
        a=(num)
        if(a[0]=='+'):
            solution= eval(lastnumber+a)


        elif(a[0]=='-'):
             solution= eval(lastnumber+a)

        elif(a[0]=='*'):
            number=int(a[1:])
            lastnumberx=int(lastnumber)
            solution=(lastnumberx*number)
        elif(a[0]=='/'):
            number=int(a[1:])
            lastnumberx = int(lastnumber)
            solution = (lastnumberx / number)

        else:
            solution=eval(a)

        return(solution)
    except SyntaxError:
        return("No expression after the the given number")

    except ZeroDivisionError:
        return("cant divide with 0!!!!")
    except IndexError:
        return("No expression entered, Please enter something!!!!")

    except NameError:
        l=a[4:-1]
    if a[0]=='s':
        return(math.sin(float(l)))
    elif a[0]=='c':
        return(math.cos(float(l)))

    elif a[0]=='t':
        return(math.tan(float(l)))
    elif a[0]=='l':
        return(math.log(float(l),10))




k=func(lastnumber)

print(k)






logging.basicConfig(filename="log.txt",format='%(asctime)s %(message)s',filemode='a+')


logger1 = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger1.setLevel(logging.DEBUG)
handler=logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)


logger1.setLevel(logging.DEBUG)
handler=logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter1=logging.Formatter('%(asctime)s-%(message)s')
handler.setFormatter(formatter1)
logger1.addHandler(handler)
logger1.info('This is our input:-------'+ lastnumber+'\t'+ '||||||||||       This is our output:-------' +str(k))


