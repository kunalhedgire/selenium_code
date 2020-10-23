input_string = "kunal has good man"

# words = str1.split()
# for word in words:
#     print(''.join(word[::-1]), end=" ")

def rever(input_string):

    for i in range(len(input_string)):
            if input_string[i].isupper():
                return input_string[i].lower()
            elif input_string.islower():
                return input_string.upper()
            else:
                return input_string[i]



print(rever("kunal has good man"))

# class bank:
#     def __init__(self, id, balance):
#         self.id = id
#         self.balance = balance
#
#     def withdrawn(self, amount):
#         self.balance -= amount
#
#     def deposit(self, amount):
#         self.balance += amount
#
# acc = bank('123', 100)
# acc.deposit(800)
# acc.withdrawn(500)
#
# fname = "%s" % acc.id
# fd = open(fname, "w")
# ss = str(acc.balance)
# fd.write(ss)
# fd.close()
#
# acc.deposit(200)
# fd = open(fname, "rb")
# print(fd.readlines()[0])
# fd.close()
#
# print(acc.balance)
#


def reverse_words(input_string):
    par = ""
    words = input_string.split()
    for word in words:

        if word.istitle():
            par = par + " " + word[::-1].title()
        else:
            par = par + " " + word[::-1]

    return par.lstrip()


print(reverse_words("I am work at Nutanix"))


















