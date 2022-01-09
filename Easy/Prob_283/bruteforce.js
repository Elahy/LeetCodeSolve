/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  let slow = 0,
    fast = 0;
  while (slow < nums.length) {
    if (fast === nums.length) {
      nums[slow] = 0;
      slow += 1;
    } else if (nums[fast] !== 0) {
      nums[slow] = nums[fast];
      slow += 1;
      fast += 1;
    } else {
      fast += 1;
    }
  }
};
