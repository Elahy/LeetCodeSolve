/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function (m, n) {
  let row = new Array(n).fill(1);
  for (let r = m - 2; r > -1; r--) {
    for (let c = n - 2; c > -1; c--) {
      row[c] += row[c + 1];
    }
  }
  return row[0];
};
