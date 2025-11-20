
# file_path = "/st.txt"
# #
# with open(file_path, "r") as file:
#     print(file.read())
# count = 0
# with open("st.txt", "r") as file:
#     for line in file:
#         print(line)
#         # count += 1
#         print(len(file.readlines()))
#         # print(file.)
# # print(count)

# file_path = "/st.txt"
# with open(file_path, "r") as file:
#     lines = file.readlines()
#     print(len(lines)
#     for i in lines:
#         print(i)


# file_path = "/st.txt"
# def read():
#     with open(file_path, "r") as file:
#         for message in file:
#             print(message, end="")
#     print()
#
# print(read("st.txt", "привет" ))



# file_path = "/st.txt"

import re


# def count_world_in_file(path, world):
#
#     with open(path, "r", encoding="utf-8") as file:
#         text = file.read()
#         listik = re.split(r"[\s\n]", text)
#         print(listik)
#
#         counter = 0
#         for i in  listik:
#             if i == "пока":
#                 counter +=1
#         return counter
# print(count_world_in_file()   )

# def file_copy(path):
#
#     with open(path, "r", encoding="utf-8") as file:
#         text = file.read()
#     new_path = path[:index]+"(copy).txt"
#     with open(new_path, 'w', encoding="utf-8") as file:
#         file.write("text")

vocabular = ("ой" "уй")
path = "/st.txt"

def censore(path):

    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
        result_list = re.split(r"[\s\n]", text)


