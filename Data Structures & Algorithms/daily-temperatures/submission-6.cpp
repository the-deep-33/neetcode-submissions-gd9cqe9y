class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> sol_stack;
        vector<int> sol_vector(temperatures.size(), 0);

        for(int i = 0; i < temperatures.size(); ++i)
        {
            while(!sol_stack.empty())
            {
                if(temperatures[i] > sol_stack.top().second)
                {
                    sol_vector[sol_stack.top().first] = i - sol_stack.top().first;
                    sol_stack.pop();
                }
                else{
                    break;
                }
            }
            sol_stack.push(make_pair(i, temperatures[i]));
        }

        return sol_vector;
    }
};
