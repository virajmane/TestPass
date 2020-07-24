import re

p = str(input("Enter Password\n"))
lst = ["123456","123456789","qwerty","password","111111""12345678","abc123","1234567","password1","12345","Pass123","Passd@123","123","abcd123","abcdqwer","Pass@123"]
exp1 = re.compile(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#%_-])[a-zA-Z0-9@#%_-]{8,}")
exp2 = re.compile(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}")
exp3 = re.compile(r"(?=.*[a-z])(?=.*[A-Z])[a-zA-Z]{5,}")

case1 = exp1.search(p)
case2 = exp2.search(p)
case3 = exp3.search(p)

if p in lst:
    print("Your Password is the most commonly used Password in the World!")
elif len(p) < 8:
    print("Too Short make sure its Atleast 8 Digits Contains Uppercase,lowercase and special characters and Digits")
elif case1 != None:
    print("Your Password is Strong!")
elif case1 == None and case2 != None:
    print("Please include a special character in it")
elif case3 != None:
    print("Use Digits And Special Characters in your password")