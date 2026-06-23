class Solution {
public:
    int countPrimes(int n) {
        vector<bool> prime(n, true);
        int count = 0;
        for(int i=2;i<n;i++){
            if(prime[i]){
                count++;
                for(long long j=1LL*i*i;j<n;j+=i)
                    prime[j]=false;
            }
        }
        return count;
    }
};