/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
  if (nums.length == 1) {
    return nums[0];
  }
  let maxProd = 1,
    minProd = 1,
    best = 0;

  for (i = 0; i < nums.length; i++) {
    if (nums[i] < 0) {
      let temp = maxProd;
      maxProd = minProd;
      minProd = temp;
    }
    maxProd = Math.max(maxProd * nums[i], nums[i]);
    minProd = Math.min(minProd * nums[i], nums[i]);

    best = Math.max(maxProd, best);
  }

  return best;
};
