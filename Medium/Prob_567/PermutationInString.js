/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function (s1, s2) {
  let ls1 = s1.length;
  if (ls1 > s2.length) return false;
  const isZero = function (checker) {
    for (i in checker) {
      if (checker[i]) return false;
    }
    return true;
  };

  let checker = new Array(26).fill(0);

  for (let j = 0; j < ls1; j++) {
    checker[s1.charCodeAt(j) - 97]++;
  }

  for (let k = 0; k < s2.length; k++) {
    checker[s2.charCodeAt(k) - 97]--;
    if (k - ls1 >= 0) checker[s2.charCodeAt(k - ls1) - 97]++;
    if (isZero(checker)) return true;
  }
  return false;
};
