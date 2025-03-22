/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head)
{
    struct ListNode *cur=head;

    while(cur!=NULL && cur->next!=NULL)
    {
        if(cur->val==cur->next->val)
        {
            struct ListNode *temp=cur->next;
            cur->next=cur->next->next;
            free(temp);
        }
        else
        {
            cur=cur->next;
        }
    }
    return head;
}

/*
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
*/
