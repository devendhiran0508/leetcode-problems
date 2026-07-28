class Solution {
public:
    string smallestPalindrome(string s) {
        int n = s.length();
        int k = n / 2;
        string left = s.substr(0, k);
        sort(left.begin(), left.end());
        string mid = (n % 2 != 0)? string(1, s[k]): "";
        string right = left;
        reverse(right.begin(), right.end());
        return left + mid + right;
    }
};