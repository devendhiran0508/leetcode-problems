class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        int n1 = INT_MAX, n2 = INT_MIN;
        for (int x: nums) {
            n1 = min(n1,x);
            n2 = max(n2,x);
        }
        return (long long)(n2 - n1) * k;
    }
};