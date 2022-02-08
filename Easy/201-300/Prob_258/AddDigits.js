/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function (num) {
  let temp = 0;
  while (num >= 10 || temp > 0) {
    if (num < 10) {
      num += temp;
      temp = 0;
    } else {
      temp += num % 10;
      num = Math.floor(num / 10);
    }
  }
  return num;
};
