class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        sort(piles.begin(), piles.end());

        int low = 1;
        int high = piles[piles.size() - 1];

        int potential = -1;

        bool found = false;

        while(low <= high)
        {
            if(low == high)
            {
                if(found == false)
                {
                    found = true;
                }
                else{
                    break;
                }
            }
            int mid = (low + high) / 2;
            
            int iter = 0;
            for(int i = 0; i < piles.size(); ++i)
            {
                iter += piles[i] / mid;
                if(piles[i] % mid != 0){
                    ++iter;
                }
            }
            if(iter <= h)
            {
                potential = mid;
                high = mid;
            }
            else if(iter > h)
            {
                low = mid + 1;
            }
        }
        return potential;
    }
};
