a = ["zaid", "asima"]
a = 23
a = 5j
# name@gmail.com

def email_maker(name):
    return f"{name}@gmail.com"

email_a = map(email_maker, a)

[print(x) for x in email_a]
