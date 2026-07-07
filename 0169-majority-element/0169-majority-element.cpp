class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int cnt = 0;
        int ele1 = 0;

        for (int ele : nums) {
            if (cnt == 0) {
                ele1 = ele;
            }

            if (ele1 == ele) {
                cnt++;
            }
            else {
                cnt--;
            }
        }
        return ele1;
    }
};