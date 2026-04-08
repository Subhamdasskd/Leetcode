#include <vector>
using namespace std;

class Solution {
public:
    static constexpr int MOD = 1'000'000'007;

    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        for (const vector<int>& query : queries) {
            int left = query[0];
            int right = query[1];
            int step = query[2];
            int value = query[3];

            for (int index = left; index <= right; index += step) {
                nums[index] = static_cast<int>(1LL * nums[index] * value % MOD);
            }
        }

        int answer = 0;
        for (int num : nums) {
            answer ^= num;
        }

        return answer;
    }
};