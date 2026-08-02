class TimeMap {
    unordered_map<string, map<int, string>> feeling_map;
public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        feeling_map[key].insert({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        int low = 0;
        int high = feeling_map[key].size();

        string candidate = "";

        while(low < high)
        {
            int mid = low + (high-low) / 2;
            auto it = feeling_map[key].begin();

            advance(it, mid);
            int time = it->first;

            if(timestamp == time)
            {
                candidate = it->second;
                return candidate;
            }
            else if(timestamp > it->first)
            {
                candidate = it->second;
                low = mid + 1;
            }
            else{
                high = mid;
            }
        }
        return candidate;
    }
};
