class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int counter = count(nums.begin(), nums.end(), 0);
        if(counter > 1)
        {
            vector<int> zeros(nums.size());
            return zeros;
        }
        else if(counter == 1)
        {
            int prod = 1;
            vector<int> sol_vector;
            if(nums.size() == 1)
            {
                return {0};
            }
            int t = -1;
            for(int i = 0; i < nums.size(); ++i)
            {
                if(nums[i] != 0)
                {
                    prod *= nums[i];
                }
                else{
                    t = i;
                }
            }
            vector<int> zeros(nums.size());
            zeros[t] = prod;
            return zeros;
        }
        else{
            vector<int> sol_vector;
            if(nums.size() == 1)
            {
                return {nums[0]};
            }
            int prod = 1;
            for(int i = 1; i < nums.size(); ++i)
            {
                prod *= nums[i];
            }
            sol_vector.push_back(prod);
            for(int i = 1; i < nums.size(); ++i)
            {
                prod /= nums[i];
                prod *= nums[i-1];
                sol_vector.push_back(prod);
            }
            return sol_vector;
        }
    }
};
