# #  1
# # summa = 0
# # counter = 0
# # while True:
# #     counter += 1
# #     number = int(input())
# #     if number == 0:
# #         break
# #
# #     summa += number
# #     average = summa/counter
# # print(summa)
# # print(average)
# import random
#
#
# #2
#
# def min_in_list(_list):
#     minimum = _list[0]
#     for i in _list:
#         if minimum > 1:
#             minimum = 1
#     return minimum
#
# #3
#
# def create_list():
#     list1=[0,0,0,0,0,0,0,0,0,0]
#     list1[i]=random.randint(1,10)
#     return list1
#
# #4
#
# def list_append(list1, list2):
#     list3=[]
#     for i in list1:
#         list3.append(i)
#     for i in list2:
#         list3.append(i)
#
# #5
# def pop_el(list1, index):
#     list2=[]
#     for i in range(index):
#         list2.append(list1[i])
#     for i in range(index+1, len(list1)):
#         list2.append((list1[i]))
#     return list2
# #6
# def max_index(list1):
#     maximum=list1[0]
#     index_maximum = 0
#
#     for i in (len(list1)):
#         if maximum < list1[i]:
#             maximum = list1[i]
#             index_maximum = i
#     return index_maximum


students = [
    [11, 22, 33, 44, 55],
    [22, 33, 54, 64, 75],
    [42, 51, 63, 74, 95]
]


# for i in students[0]:
#     print(i, end=" ")
# print()
#
# for j in students[1]:
#     print(j, end=" ")
# print()
#
# for a in students[2]:
#     print(a, end=" ")
# print()

# for i in students:
#     for j in i:
#         print(j, end=" ")
#     print()

# for i in range(0, 3):
#     print(students[i][1], end=" ")
#     print()

