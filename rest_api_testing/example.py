import re
with open("input.txt", "r") as file:
    count = 0
    res = file.readlines()
    # count = res.count("Error")
    # for line in res:
    #     if "Error" in line:
    #         count += 1
    # print(count)
    r = re.search("a-z", "Error")
    print(r)



str1 = "aba"

rev_str1 = str1[::-1]

if str1 == rev_str1:
    print("pal")
else:
    print("not pal")


class emp_details:

    def __init__(self, emp_id, emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name

    def print_emp_name(self):
        print(self.emp_name)

    def print_emp_id(self):
        print(self.emp_id)

    def edit_emp_id(self, emp_id):
        print("The older emp_id is:", self.emp_id)
        return emp_id


e = emp_details(1 , "kunal")
print(e.edit_emp_id(2))
e.print_emp_id()
e.print_emp_name()



str1 = "Hello World"

dict1 = dict()

for char in str1:
    if char in dict1:
       dict1[char] += 1
    else:
        dict1[char] = 1

print(dict1)


try:
    k = 0 // 5
except:
    raise ZeroDivisionError
finally:
    print("This is always executed")

# finally:
#     print("")
print("*"*70)

list1 = []
for i in range(1, 100):
    add = ''

    if i % 3 == 0:
        add += "Fizz"

    if i % 5 == 0:
        add += "Buzz"

    if add == '':
        list1.append(i)
    else:
        list1.append(add)

for i in list1:
    print(i)
