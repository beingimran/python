import random

def gen_password ():
    l = ['@','#','$','%']
    upper = chr(random.randint(65,90))
    lower = chr(random.randint(97,122))
    special = random.choice(l)
    number = random.randint(10000,99999)
    password = lower + upper + str(number) + special + lower + str(number)

    return password




result=gen_password()
print(result)
