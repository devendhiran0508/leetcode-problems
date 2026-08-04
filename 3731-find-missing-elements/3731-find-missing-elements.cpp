class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
        int minVal = *min_element(nums.begin(), nums.end());
        int maxVal = *max_element(nums.begin(), nums.end());
        unordered_set<int> seen(nums.begin(), nums.end());
        vector<int> res;

        for (int i = minVal; i <= maxVal; ++i) {
            if (seen.find(i) == seen.end()) {
                res.push_back(i);
            }
        }
        return res;
    }
};