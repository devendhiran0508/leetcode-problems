class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        vector<int> res;
        string digit = "123456789";

        for (int len = 2; len <=9; ++len) {
            for (int start = 0; start <= 9 - len; ++start) {
                string sub = digit.substr(start, len);
                int num = stoi(sub);
                if (num >= low && num <= high) {
                    res.push_back(num);
                }
            }
        }
        return res;
    }
};