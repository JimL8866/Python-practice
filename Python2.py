fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [item for item in fruits if "a" in item]
print(new_list)

string = "BundooraMelbourne"
new_string = [chr(ord(item)) for item in string if ord(item) > 97]
print(new_string)

# list comprehension
# newlist = [expression for item in iterable if condition == True]
# iterable: list, string, dic, tuple
# expression is the item in iteration, also can contain conditions, can be manipulated



old_price = {"milk": 1.02, "coffee": 2.5, "bread": 2.5}

new_price = {key:value*1.2 for (key, value) in old_price.items()}
print (new_price)
new_dict = {key: ("cheap" if value <3 else "expense") for (key, value) in new_price.items()}

# new_dict = {key:value for (key, value) in old_dic if value }
# ternary conditional operator
# some_expression if condition else other_expression

age = 12
age_group = "Minor" if age < 18 else "Adult"
print (age_group)