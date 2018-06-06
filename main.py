#! /usr/bin/env python3
import random
import string
import tkinter

# TODO create GUI
'''top = tkinter.Tk()
top.mainloop()'''

print("---random number generator---")
print("enter character count: ")


def main():
    count = int(input())

    password = generator(count)
    print(password)


def securityCheck(password, count):
    if (any(x.isupper() for x in password) and any(x.islower() for x in password) and any(
            x.isdigit() for x in password)):  # and (password.find(" !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"))
        print("secure")
        return password
    else:
        print(password + " is not secure\nRegenerating password")
        password = generator(count)
        print(password)


def generator(count):
    password = ''
    for i in range(count):
        password += password.join(
            random.SystemRandom().choice(string.ascii_letters + " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + string.digits))

    return securityCheck(password, count)


if __name__ == '__main__':
    main()
