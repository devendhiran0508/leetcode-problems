class Solution {
public:
    bool rotateString(string s, string goal) {
        if (s.length() != goal.length())
            return false;
        string a = s + s;

        if (a.find(goal) < a.length())
            return true;
        else 
            return false;
    }
};