struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode *head=NULL;
    struct ListNode *tail=NULL;

    if(list1==NULL)
        return list2;
    if(list2==NULL)
        return list1;

    while(list1!=NULL && list2!=NULL)
    {
        struct ListNode *newnode;
        if(list1->val<=list2->val)
        {
            newnode=list1;
            list1=list1->next;
        }
        else
        {
            newnode=list2;
            list2=list2->next;
        }
        if(head==NULL)
        {
            head=newnode;
            tail=head;
        }
        else
        {
            tail->next=newnode;
            tail=newnode;
        }
        if(list1!=NULL)
        {
            if(tail==NULL)
            {
                head=list1;
            }
            else
            {
                tail->next=list1;
            }
        }
        if(list2!=NULL)
        {
            if(tail==NULL)
            {
                head=list2;
            }
            else
            {
                tail->next=list2;
            }
        }
    }
    return head;
}

/*
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
*/
