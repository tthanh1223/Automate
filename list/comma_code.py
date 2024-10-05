spam = ['apples','bananas','tofu','cats']
'''
a function that takes a list value as an argument and returns
a string will all the items separate by a comma and a space
with and inserted before the last item.
'''
def comma_str(arr:list[int]) -> str:
    comma = str()
    for i in range(0,len(arr)):
        if i < len(arr)-2:
            comma = comma + str(arr[i]) + ', '
        elif i == len(arr)-2:
            comma = comma + str(arr[i]) + ' and '
        else:
            comma = comma + str(arr[i])
    return comma
lst = [1,2,3,45,34,13,12312,312,3123,'asdfas',1,31,3123]
print(comma_str(lst))