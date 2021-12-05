/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var rob = function (root) {
  let dfs = function (root) {
    if (root == null) {
      return [0, 0];
    }

    let leftPair = dfs(root.left);
    let rightPair = dfs(root.right);

    let withRoot = root.val + leftPair[1] + rightPair[1];
    let withoutRoot =
      Math.max(leftPair[0], leftPair[1]) + Math.max(rightPair[0], rightPair[1]);

    return [withRoot, withoutRoot];
  };
  result = dfs(root);
  return Math.max(result[0], result[1]);
};
