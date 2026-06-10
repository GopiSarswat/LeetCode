class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        sort(candyType.begin(), candyType.end());
        int x = 1;
        for (int i = 1; i < candyType.size(); i++) {
            if (candyType[i] != candyType[i - 1]) {
                x++;
            }
        } 
        return min(x, (int)candyType.size() / 2);
    }
};