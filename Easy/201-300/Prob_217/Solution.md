# We are using set to keep track of duplicate

# We are not using Sorting as Sorting the list take O(nlogn) and we can do it in O(n) time using set

First we are taking a set named Checker

Then we are traversing the whole array and checking if the number is already present in the checker,
if it does we Directly1 return True
Otherwise we add that number to the Checker set.
