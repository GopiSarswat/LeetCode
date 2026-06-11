#include<algorithm>
class Solution {
public:
    int search(vector<int>& nums, int target) { 
        auto it = std::lower_bound(nums.begin(), nums.end(), target);
        return (it != nums.end() && *it == target) ? std::distance(nums.begin(), it) : -1;
    }
};