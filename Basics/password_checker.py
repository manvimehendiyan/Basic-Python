def check_pass(password):
    valid=1
    special=0
    upper=0
    lower=0
    digit=0
    if len(password)<6:
        print("Minimum length of password is 6 characters.")
        valid=0
    if len(password)>16:
        print("Maximum length of password is 16 characters.")
        valid=0
    for x in password:
        if(x=='$' or x=='#' or x=='@'):
            special=1
        if x.isupper():
            upper=1
        if x.islower():
            lower=1
        if x.isdigit():
            digit=1
    if digit==0:
        print("Password must have atleast 1 number between [0-9].")
        valid=0
    if lower==0:
        print("Password must have atleast 1 letter between [a-z]. ")
        valid=0
    if upper==0:
        print("Password must have atleast 1 letter between [A-Z]. ")
        valid=0
    if special==0:
      print("Password must have atleast 1 character from [$#@].")  
      valid=0
    return valid

password=input("Enter your Password: ")
n=check_pass(password)
if n==1:
    print("Valid Password")
elif n==0:
    print("Invalid Password!")
