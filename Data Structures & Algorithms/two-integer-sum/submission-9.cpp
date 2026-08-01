class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> lost_and_found;
        lost_and_found[nums[0]] = 0;
        vector<int> result;

        for(int i = 1; i < nums.size(); ++i)
        {
            int potential = target - nums[i];
            auto it = lost_and_found.find(potential);

            if(it != lost_and_found.end())
            {
                // result.push_back(lost_and_found[potential]);
                // result.push_back(i);
                return {lost_and_found[potential], i};
            }
            lost_and_found[nums[i]] = i;
        }
    }
};
