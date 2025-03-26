/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
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