/**
 * @param {number} n
 * @return {number}
 */
var bitwiseComplement = function (n) {
  return (2 << Math.log2(n)) - 1 - n;
};
