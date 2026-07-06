class Solution {
public:
    int minimumSwaps(vector<int>& nums) {
        int total_zeros = count(nums.begin(), nums.end(), 0);

        if (total_zeros == 0 || total_zeros == nums.size())
            return 0;
        
        int misplaced_non_zero = 0;
        int n = nums.size();
        for (int i = n - total_zeros; i < n; i++) {
            if (nums[i] != 0) {
                misplaced_non_zero++;
            }
        }
        return misplaced_non_zero;
    }
};