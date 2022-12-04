GITimport sys
sys.path.append('/mymodules/')
import mymodules
from mymodules.mathy import *
print(responses[0])
print(responses[1])
while True:
    print()
    text=input("Hi! How may I help You ==> ")
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l=extract_numbers_from_text(text)
                r=operations[word.upper()](l[0],l[1])
                print(r)
            except:
                print("Sorry But something went wrong ,Please Retry ")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()] ()  
            break
    else:
        sorry()                
