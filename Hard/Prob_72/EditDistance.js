/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function (word1, word2) {
  let m = word1.length;
  let n = word2.length;
  const dp = new Array(m + 1);

  for (let k = 0; k < dp.length; k++) dp[k] = new Array(n + 1).fill(Infinity);

  for (let c = 0; c <= n; c++) dp[m][c] = n - c;

  for (let r = 0; r <= m; r++) dp[r][n] = m - r;

  for (let i = m - 1; i >= 0; i--) {
    for (let j = n - 1; j >= 0; j--) {
      if (word1[i] === word2[j]) dp[i][j] = dp[i + 1][j + 1];
      else
        dp[i][j] = 1 + Math.min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1]);
    }
  }
  return dp[0][0];
};
