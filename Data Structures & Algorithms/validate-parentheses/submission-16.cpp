class Solution {
public:
    bool isValid(string s) {
        stack<char> sol_stack;
        string add_stack = "{([";

        for(int i = 0; i < s.length(); ++i)
        {
            if(add_stack.contains(s[i]))
            {
                sol_stack.push(s[i]);
            }
            else{
                if(sol_stack.empty() || sol_stack.size() < 1) 
                    return false;

                char compare = sol_stack.top();
                sol_stack.pop();
                if(compare == '[' && s[i] == ']')
                {
                    continue;
                }
                else if(compare == '{' && s[i] == '}') continue;
                else if(compare == '(' && s[i] == ')') continue;
                else{
                    return false;
                }
            }
        }
        if(sol_stack.empty()){
            return true;
        }
        return false;
    }
};
