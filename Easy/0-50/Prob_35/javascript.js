/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
  start = 0;
  end = nums.length;
  while (start < end) {
    mid = Math.floor((start + end) / 2);
    if (nums[mid] < target) {
      start = mid + 1;
    } else {
      end = mid;
    }
  }
  return start;
};
