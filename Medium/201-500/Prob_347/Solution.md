# Here We are using 2 Hashmap to Solve this Problen in O(n) time Complexity

In First Hashmap we are Calculating the Frequency of the Elements in the given array

In Second Hashmap we are Storing the frequency of the first hashmap as key and the the nums that occurs that frequency we store them in an array.

Finally run a loop from the length of th given array,
because the maximum frequency of a element can be the length of the given array.

so we are picking the highest frequent element and storing them in result array

We return the subarray of result array upto k-1 length.
