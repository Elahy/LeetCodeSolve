/**
 * @param {string} s
 * @return {number}
 */
var maxPower = function (s) {
  let left = 0,
    right = 1,
    count = 1,
    maxLen = 1;

  while (right < s.length) {
    if (s[left] == s[right]) {
      count++;
      maxLen = Math.max(count, maxLen);
      right++;
    } else {
      left = right;
      right++;
      count = 1;
    }
  }
  return maxLen;
};
