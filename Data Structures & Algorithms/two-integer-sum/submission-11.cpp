class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> lost_and_found;

        for(int i = 0; i < nums.size(); ++i)
        {
            int potential = target - nums[i];
            auto it = lost_and_found.find(potential);

            if(it != lost_and_found.end())
            {
                return {lost_and_found[potential], i};
            }
            lost_and_found[nums[i]] = i;
        }
    }
};
