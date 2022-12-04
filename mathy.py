responses=[" Welcome to '' SMART CALCULATOR ''","... My name is 'SHASH'...","THANKS","SORRY, This is beyond my ability","My Pleasure 😊"]
def extract_numbers_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)
def LCM(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
def HCF(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
def add(a,b):
    return a+b
def sub(a,b):
    return a-b 
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def mod(a,b):
    return a%b
def greater(a,b):
    if (a>b):
     return a
    elif(a<b):
     return b
def small(a,b):
    if (a>b):
        return b
    elif(a<b):
        return a
def end():
    print(responses[2])
    input("press ENTER key to 'Exit' ")
    exit()
def table():
    n=int(input("Enter a no ="))
    for i in range(1,11):
        print(i*n)
def square():
    n=int(input("Enter a no ="))
    print(f"Square of {n} is =",n*n)
    
def cube():
    n=int(input("Enter a no ="))
    print(f"Cube of {n} is =",n*n*n)
def myname():
    print(responses[1])
def sorry():
    print(responses[3])
def thank():
    print(responses[4])
operations={"MODULO":mod,"GREATER":greater,"BIGGER":greater,"BIG":greater,"SMALLER":small,"LESSER":small,"SMALL":small,"MODULUS":mod,"MOD":mod,"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"MINUS":sub,"SUBTRACTION":sub,"SUBTRACT":sub,"DIFFERENCE":sub,"MULTIPLICATION":multiply,"MULTIPLY":multiply,"INTO":multiply,"DIVIDE":division,"DIVISION":division,"LCM":LCM,"HCF":HCF}
commands={"THANK":thank,"THANKS":thank,"NAME":myname,"END":end,"EXIT":end,"CLOSE":end,"TABLE":table,"SQUARE":square,"CUBE":cube}

