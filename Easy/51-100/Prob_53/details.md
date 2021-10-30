Problem: 53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

Solution:
To solve this let's take to variable
one for largest sum so far, here we call in largest
another for max sum at the end of iteration, here maxending

initiallily both has value of the first element of the nums array

let take a array runner variable i and set it to second index of nums array

here we are using a while loop till the last index of the nums array

In each iteration we are checking current itaretion value is bigger than maxending and current iteration value combined and set in to maxending
