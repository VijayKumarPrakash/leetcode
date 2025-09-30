def eliminateSubstring(s, part):
    while part in s:
        s = s.replace(part, "")
    return s

## Why is it better to use a list instead of directly working with strings?
## This is because Python strings are immutable, so when we append characters
## to the end of a string, it actually creates a new string, i.e. complexity = O(n)
## However, when we append an element to a list, the complexity is O(1)

def eliminateSubstringUsingList(s, part):
    result = []
    part_length = len(part)
    part_list = list(part)

    for char in s:
        result.append(char)

        if result[-part_length:] == part_list:
            result = result[:-part_length]
    
    return "".join(result)

# Get input from user
s = input("Enter the main string: ")
part = input("Enter the substring to eliminate: ")
s
# Predefined inputs
# s = 'ababcabccabcaa'
# part = 'abc'

result = eliminateSubstring(s, part)
print("Resulting string:", result)

result2 = eliminateSubstringUsingList( s, part)
print("Resulting string using list:", result)
