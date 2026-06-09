class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int j = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                int x = nums[i];
                nums[i] = nums[j];
                nums[j] = x;
                j++;
            }
        }
    }
};