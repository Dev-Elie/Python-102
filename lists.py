# List : a collection which is ordered and changeable. Allows duplicate members.

# Creating a new list
numbers = list()  # New empty list
numbers = []  # New empty list
languages = ["Python", "Java", "C++", "C#", "JavaScript"]  # New list with values

# Accessing list items
print(languages[0])  # print first item
print(languages[-1])  # print the last item in the list
print(languages[0:3])  # print the first three items in the list
print(languages[:3])  # same as above
print(languages[2:])  # prints from the second item to the end of the list
print(languages[-3:])  # prints from the third to the last item in the list
print(languages[::2])  # prints every second item in the list(steps of 2)
print(languages[::-1])  # reverse
print(languages[::-2])  # prints every second item in the list in reverse order

#### Adding items to a list
languages.append("C")  # add a new item to the end of the list
languages.insert(5, "Go")  # insert a new item at the specified index
languages.extend(["Ruby", "PHP"])  # add a list of items to the end of the list
languages.append(["Python", "Java", "C++", "C#", "JavaScript"])  # add a list of items to the end of the list


### Iterate through a list
for i in languages:
    print(i)

for i in range(len(languages)):
    print(languages[i])

print("Python" in languages)  # check if an item is in the list
print("C" not in languages)  # check if an item is not in the list

print(len(languages) == 0)  # check if the list is empty

# use if statements to check if a list is empty
if len(languages) == 0:
    print("The list is empty")
else:
    print("The list is not empty")


# remove an item from the list
languages.remove("Python")  # remove the first instance of Python
languages.pop()  # removes the last item in the list and returns it
languages.pop(0)  # removes the item at the specified index and returns it
del languages[0]  # delete the first item in the list
del languages[-1]  # delete the last item in the list

languages.clear()  # clear the list

languages.reverse()  # reverse the list
languages.sort()  # sort the list in ascending order (A-Z) or descending order (Z-A) (default) replace with reverse=True for descending order
newsorted = sorted(languages)  # sort the list in a new list and return it (sorted is a function) returns a sorted copy of the list
languages.sort(reverse=True)  # sort the list in reverse order
languages.sort(key=str.lower)  # sort the list by the lowercase version of the items/alphabetically
languages.sort(key=str.lower, reverse=True)  # sort the list by the lowercase version of the items/alphabetically in reverse order
languages.count("Python")  # count the number of times the specified item occurs in the list
languages.index("Python")  # return the index of the first occurrence of the specified item
print(languages.split())  # split the list into a list of strings

languages[0:2] = ["Python", "C++"]  # replace the first two items in the list

languages.reverse()  # reverse the list


##### make copy of a list

languages_copy = languages.copy()  # make a copy of the list using the copy() method
languages_copy1 = list(languages)  # make a copy of the list using list()
languages_copy2 = languages[:]  # make a copy of the list using slicing

# List comprehension
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlist = [x * x for x in mylist]  # square each number in the list
