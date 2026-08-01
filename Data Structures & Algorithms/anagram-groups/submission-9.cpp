class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map <string, vector<string>> sol_map;
        vector<vector<string>> sol_vector;

        for(int i = 0; i < strs.size(); ++i)
        {
            cout << "i = " << i << endl;
            string str = strs[i];
            sort(str.begin(), str.end());
            sol_map[str].push_back(strs[i]);
        }

        for(auto it = sol_map.begin(); it != sol_map.end(); ++it)
        {
            sol_vector.push_back(it->second);
        }

        return sol_vector;
    }
};
