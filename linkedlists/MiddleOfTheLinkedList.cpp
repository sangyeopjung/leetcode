// https://leetcode.com/problems/middle-of-the-linked-list/description/
// tags: linked list, two pointers

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head)
    {
        ListNode* out = new ListNode(0, head);
        ListNode* fast = out;
        ListNode* slow = out;
        while (fast && fast->next)
        {
            fast = fast->next->next;
            slow = slow->next;
        }

        return fast ? slow->next : slow;
    }
};