# 11. Container With Most Water

#### Difficulty Status: Medium

### Problem Statement

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

### Example 1:

**Input:** height = [1,8,6,2,5,4,8,3,7] <br />
**Output:** 49 <br />
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

### Example 2:

**Input:** height = [1,1] <br />
**Output:** 1

### Constraints:

n == height.length <br />
2 <= n <= 105 <br />
0 <= height[i] <= 104 <br />

## Explanation :

Although this problem is about water volume but we are actually calculating the maximum area. If we think about this in 2D space instead of 3D this might help.

We get a list of different height in the input and we take 2 height from that list possibly from the further apart so that the distance between those height are maximum. We calculate the area by multiplying the height and the distance.

### Code :

```Python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        water = 0

        while i < j:
            water = max(water, (j-i)*min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water
```

here we take two pointer, one at the begin of the height list ( i ) and another at the end of the list ( j ) and another variable to store the area ( water )
