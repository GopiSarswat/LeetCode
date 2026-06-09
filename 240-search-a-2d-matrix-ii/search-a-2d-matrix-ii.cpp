class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        bool x = 0;
        for(int i = 0; i < matrix.size(); i++){
            for(int j = 0; j < matrix[0].size(); j++){
                if(target == matrix[i][j]){
                    x = 1;
                    break;
                }
            }
        }
        return x;
    }
};