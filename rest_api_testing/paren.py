# def sum_num(arr, num):
#
#     dict1 = dict()
#
#     for i in arr:
#         minus_ele = num - i
#
#         if minus_ele in dict1:
#             return True
#         dict1[i] = True
#
#
# a = sum_num([10, 2, 6, 7, 5, 3], 8)
# print(a)


def second_max(arr):

    max1 = arr[0]
    max2 = arr[1]

    for i in range(2, len(arr)):
        if max1 < arr[i]:
            max1, max2 = arr[i], max1

        elif arr[i] > max2:
            max2 = arr[i]
    return max2


# print(second_max([10, 20, 30, 40, 11]))


def fizz_ball():

    list1 = []
    for i in range(1, 20):
        add = ""
        if i % 3 == 0:
            add += "Fizz"

        if i % 5 == 0:
            add += "ball"

        if not add:
            list1.append(i)
        else:
            list1.append(add)

    return list1


# print(fizz_ball())


def calculate_number_digit(string):
    char_count = 0
    digit_count = 0
    for char in string:
        if char.isdigit():
            digit_count += 1

        elif char.isalpha():
            char_count += 1

    return char_count, digit_count


# print(calculate_number_digit("kunal123!"))







l1 = [12, 12, 20, -89, 20,-20, 100, 55, -55, -10, 10]

max1 = l1[0]
max2 = l1[0]

for num in l1:
    if num > max1:
        max1, max2 = num, max1

    elif num > max2:
        max2 = num

print(max2)


min1 = l1[0]
min2 = l1[0]

for num in l1:
    if num < max1:
        min1, min2 = num, min1

    elif num < min2:
        min2 = num

print(min2)



class operator_overloading:

    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a


ob1 = operator_overloading("abc")
ob2 = operator_overloading("def")
print(ob1+ob2)



















