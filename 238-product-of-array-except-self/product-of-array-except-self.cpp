class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> x(nums.size());
        vector<int> p(nums.size(), 1);
        vector<int> s(nums.size(), 1);

        for(int i = 1; i < nums.size(); i++)
            p[i] = p[i - 1] * nums[i - 1];
    
        for(int i = nums.size() - 2; i >= 0; i--)
            s[i] = s[i + 1] * nums[i + 1];
          
        for(int i = 0; i < nums.size(); i++)
            x[i] = p[i] * s[i];
    
        return x;
    }
};