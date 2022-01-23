/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function (s, t) {
  let sc = "",
    tc = "",
    l = Math.max(s.length, t.length);
  for (let i = 0; i < l; i++) {
    if (s[i] != null) {
      if (s[i] === "#") sc = sc.substring(0, sc.length - 1);
      else sc += s[i];
    }
    if (t[i] != null) {
      if (t[i] === "#") tc = tc.substring(0, tc.length - 1);
      else tc += t[i];
    }
  }
  return sc === tc;
};
