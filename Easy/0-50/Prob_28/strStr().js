/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function (haystack, needle) {
  if (needle.length == 0) {
    return 0;
  }
  if (haystack.length == 0) {
    return -1;
  }

  let indexOccurence = haystack.indexOf(needle);
  return indexOccurence;
};
