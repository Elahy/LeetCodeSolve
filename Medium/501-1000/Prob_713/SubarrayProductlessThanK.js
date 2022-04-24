/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function (nums, k) {
  let prod = 1,
    lo = 0,
    res = 0;

  for (let hi = 0; hi < nums.length; hi++) {
    prod = prod * nums[hi];
    while (prod >= k && lo < nums.length) {
      prod = prod / nums[lo];
      lo++;
    }
    if (lo < nums.length) res += hi - lo + 1;
  }
  return res;
};
