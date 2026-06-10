class Solution {
public:
    bool canJump(vector<int>& nums) {
                int x = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (i > x)
                return 0;
            x = max(x, i + nums[i]);
            if (x >= nums.size() - 1)
                return 1;
        }
        return 1;
    }
};