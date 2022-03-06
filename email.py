# 1. lenght
#2. first letter alph
#3. @ should, and  one time
#4. 3rd and 4th -1 index .
#5. for loop and check space, alpha-upper, isdigit,

email = input("Enter a email: ")
j,k,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-3]==".") ^ (email[-4]=="."):
                for i in email:
                    if i==i.isspace():
                        j==1
                    elif i==i.isalpha():
                        if i==i.upper():
                            k==1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d==1
                if j==1 or k==1 or d==1:
                    print("wrong email 5")
                else:
                    print("good")
            else:
                print("wrong email 4")
        else:
            print("Wrong email 3")
    else:
        print("wrong email 2")
else:
    print("wrong email 1")