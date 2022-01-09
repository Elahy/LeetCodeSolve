/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function (s) {
  const stack = [];
  let curNum = 0,
    curStr = "",
    num = 0,
    str;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "[") {
      stack.push(curStr);
      stack.push(curNum);
      (curNum = 0), (curStr = "");
    } else if (s[i] === "]") {
      num = stack.pop();
      str = stack.pop();
      curStr = str + curStr.repeat(num);
    } else if (Number(s[i]) || s[i] === "0") {
      curNum = curNum * 10 + parseInt(s[i]);
    } else {
      curStr += s[i];
    }
  }
  return curStr;
};
