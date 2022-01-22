my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = int(input("Please put a number\n"))

# for i in range(len(my_list)):
#     found = my_list[i] == to_find
#     if found:
#         break
#
# if found:
#     print("Element found at index", i)
# else:
#     print("absent")
try:
    foo = my_list.index(to_find)
    if foo:
        print(f"The index of list is {foo}")
except ValueError:
    print(f"{to_find} is not in the list")