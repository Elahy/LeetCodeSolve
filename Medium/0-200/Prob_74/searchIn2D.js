/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
  if (target === matrix[0][0]) return true;

  let col = matrix[0].length;
  let start = 0;
  let end = matrix.length * col - 1;
  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    if (target === matrix[Math.floor(mid / col)][Math.floor(mid % col)])
      return true;
    else if (target < matrix[Math.floor(mid / col)][Math.floor(mid % col)])
      end = mid - 1;
    else start = mid + 1;
  }
  return false;
};
