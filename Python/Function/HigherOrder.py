#Higher Order Function
"""-----------------------
    1)Take another function as an argument or
    2)Return a function as it's output
used to make more flexible and reusable , and dynamic.  """

def build_mail(username,provider):
    if provider == "gmail":
        return f"{username}@gmail.com"
    elif provider == "outlook":
        return f"{username}@outlook.com"
    elif provider == "zoho":
        return f"{username}@zoho.com"

print(build_mail("sivaprakashh","gmail"))
print(build_mail("sivaprakashh","gmail"))
print(build_mail("sivaprakashh","gmail"))
print(build_mail("sivaprakashh","gmail"))
print(build_mail("sivaprakashh","gmail"))
print(build_mail("sivaprakashh","gmail"))

#type - 1
""" Take Another function as a argument """


def google(username):
    return f"welcome to google {username}"
def facebook(username):
    return f"welcome to google {username}"
def amazon(username):
    return f"welcome to google {username}"

def build_fun(username,provider_fun):
    return provider_fun(username)
print(build_fun("sivaprakash",google))
print(build_fun("aji",google))
print(build_fun("prakash",google))


#Type-2 Return function

def email_builder(domain):
    def build_email(username):
        return f"{username}@{domain}"
    return build_email
gmail=email_builder("gmail.com")  #pre bound logic
print(type(gmail))
face=email_builder("facebook.com")
zoho=email_builder("zoho.com")

print(gmail("siva"))


#impure fun
""" Side effect of function outside that is impure function"""
count=0
def sum():
    global count;
    count=2
    print("add",count)
def test():
    print(count)

sum()
test()
"""   sum ==> function change the count value over all , so is called impure function"""





























