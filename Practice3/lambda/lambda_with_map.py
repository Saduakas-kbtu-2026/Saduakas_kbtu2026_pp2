#The map() function applies a function to every item in an iterable:
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled) # doubles all entries in list
#                 what to do with | with what to do it with
reduced = list(map(lambda x: x - 5, numbers))
