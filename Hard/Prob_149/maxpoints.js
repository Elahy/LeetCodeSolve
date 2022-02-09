/**
 * @param {number[][]} points
 * @return {number}
 */
var maxPoints = function (points) {
  let n = points.length,
    maxpoints = 0;
  if (n < 3) return n;

  for (let i = 0; i < n - maxpoints - 1; i++) {
    const map = {},
      [x1, y1] = points[i];
    let curMax = 0;
    for (let j = i + 1; j < n; j++) {
      const [x2, y2] = points[j];
      let slope = 0;
      if (x2 - x1 == 0) slope = "Inf";
      else slope = (y2 - y1) / (x2 - x1);

      map[slope] ? map[slope]++ : (map[slope] = 1);
      curMax = Math.max(curMax, map[slope]);
    }
    maxpoints = Math.max(maxpoints, curMax);
  }
  return maxpoints + 1;
};
