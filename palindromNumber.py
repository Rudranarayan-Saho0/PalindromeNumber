#Function To Check A NUmber Is Palindrom
def Palindrom(number):
    #Convert The Number To A String
    str_num = str(number)
    #Reverse The String And Compare The Original
    return str_num == str_num[::-1]

#User Input
num = int(input("Enter A Number"))

#Check If The Number Is Palindrom
if Palindrom(num):
    print(f"{num} Is a Palindrom Number")

else:
    print(f"{num} Is Not a Palindrom Number")




#A Palindrom Number Is A Number That Remains The Same When It's Digits are Reversed.
#A Word, Verse Or Sentence (Such as: "Able was i ere i saw Elba") or a Number(Such As 12321) That reads The Same Backword Or Forward.
