/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let lo = 0,
    hi = height.length - 1,
    water = 0;

  while (lo < hi) {
    water = Math.max(water, (hi - lo) * Math.min(height[lo], height[hi]));
    if (height[lo] < height[hi]) lo++;
    else hi--;
  }
  return water;
};
