## Here we are using a HashMap of Dictionary to solve this

# Time complexity O(n+n) = O(n)

# Space Complexity O(n)

First we traverse the First String and store each character in Dictionary as key and 1 as it's value.
If the character is already present in the dictionary we simply increment it's value by 1

Then We traverse the second String and check if eeach char is present in the dictionary. If we find a char then we decrement it's value by 1 and delete the char from dictionay if it's value become 0,
If we don't find any char in dictionary then we directly [Return False]

Otherwise we return True at the end of program
