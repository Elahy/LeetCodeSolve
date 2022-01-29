/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  if (nums.length < 3) {
    return [];
  }

  nums.sort();
  let sol = [];
  for (i = 0; i < nums.length; i++) {
    if (nums[i - 1] == nums[i]) {
      continue;
    }
    if (nums[i] > 0) {
      break;
    }
    let target = 0 - nums[i];
    let rem = 0;
    const temp = new Map();
    const duplic = new Map();
    for (j = i + 1; j < nums.length; j++) {
      rem = target - nums[j];
      if (temp.has(rem)) {
        let combo = [nums[i], nums[j], rem];
        combo.sort();
        let checker = combo.toString();
        if (!duplic.has(checker)) {
          sol.push(combo);
          duplic.set(checker, checker);
        }
      } else {
        temp.set(nums[j], nums[j]);
      }
    }
  }

  return sol;
};
