email=input("enter email : ")
parts=email.split("@",1)
if len(parts)==2:
    print("user name is  : ",parts[0],"and domain name :",parts[1])
    
else:
    print("invalid mail format")
