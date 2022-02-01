/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
  let temp = "",
    res = [];
  const backtrack = function (op, cl) {
    if (temp.length == n * 2) {
      res.push(temp);
      return;
    }
    if (op < n) {
      temp += "(";
      backtrack(op + 1, cl);
      temp = temp.slice(0, temp.length - 1);
    }
    if (cl < op) {
      temp += ")";
      backtrack(op, cl + 1);
      temp = temp.slice(0, temp.length - 1);
    }
  };
  backtrack(0, 0);
  return res;
};
