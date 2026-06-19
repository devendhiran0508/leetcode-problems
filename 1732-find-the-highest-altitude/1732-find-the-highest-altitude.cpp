class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int curAlt = 0;
        int highPoint = curAlt;
        for (int alt_gain : gain) {
            curAlt += alt_gain;
            highPoint = max(highPoint, curAlt);
        }
        return highPoint;
    }
};