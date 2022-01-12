/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function (image, sr, sc, newColor) {
  let height = image.length,
    width = image[0].length,
    pcolor = image[sr][sc];

  const dfs = function (sr, sc) {
    if (
      sr < 0 ||
      sc < 0 ||
      sr > height - 1 ||
      sc > width - 1 ||
      image[sr][sc] === newColor ||
      image[sr][sc] != pcolor
    )
      return;
    image[sr][sc] = newColor;
    dfs(sr, sc + 1);
    dfs(sr, sc - 1);
    dfs(sr + 1, sc);
    dfs(sr - 1, sc);
  };
  dfs(sr, sc);

  return image;
};
