import string
import random
print("1 : easy")
print("2 : medium")
print("3 : hard")

plen = int(input("please enter the length"))
difficulty=input("enter the difficulty ( 1, 2, 3) :")


if difficulty == "1":
    if __name__ == "__main__": 
        s1 = string.ascii_uppercase
        s2 = string.digits

        s=[]
        s.extend(list(s1))
        s.extend(list(s2))

        random.shuffle(s)
        print ("your password is")
        print("".join(s[0:plen]))
        
if difficulty == "2":
    if __name__ == "__main__": 
        s1 = string.ascii_uppercase
        s2 = string.digits
        s3 = string.ascii_lowercase

        s=[]
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))

        random.shuffle(s)

        print ("your password is")
        print("".join(s[0:plen]))

if difficulty == "3":
    if __name__ == "__main__":
        s1 = string.ascii_uppercase

        s2=string.ascii_lowercase

        s3=string.digits

        s4=string.punctuation

        
        
        s=[]
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))

        random.shuffle(s)

        print ("your password is")

        print("".join(s[0:plen]))
   
   
