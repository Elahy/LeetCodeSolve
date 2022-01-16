/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  if (list1 && list2) {
    if (list1.val > list2.val) {
      let margedList = new ListNode(list2.val);
      margedList.next = mergeTwoLists(list1, list2.next);
      return margedList;
    } else {
      let margedList = new ListNode(list1.val);
      margedList.next = mergeTwoLists(list2, list1.next);
      return margedList;
    }
  }
  if (list1) return list1;
  if (list2) return list2;

  return list1;
};
