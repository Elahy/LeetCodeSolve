/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function (s, wordDict) {
  let dp = new Array(s.length).fill(false);
  for (let i = 0; i < s.length; i++) {
    for (let w of wordDict) {
      if (
        w == s.slice(i - w.length + 1, i + 1) &&
        (dp[i - w.length] || i - w.length == -1)
      ) {
        dp[i] = true;
      }
    }
  }
  return dp[s.length - 1];
};
