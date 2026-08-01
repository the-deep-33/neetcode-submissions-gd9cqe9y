class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<char> sol_vector;
        int sol_int = 0;
        int counter = 0;
        for(int i = 0; i < s.length(); ++i)
        {
            auto it = find(sol_vector.begin(), sol_vector.end(), s[i]);
            if(it != sol_vector.end())
            {
                sol_vector.erase(sol_vector.begin(), it+1);
                if(counter > sol_int)
                {
                    sol_int = counter;
                }
                counter = sol_vector.size() + 1;

            }
            else{
                counter++;
            }
            sol_vector.push_back(s[i]);
        }

        if(counter > sol_int)
        {
            sol_int = counter;
        }

        return sol_int;
    }
};
