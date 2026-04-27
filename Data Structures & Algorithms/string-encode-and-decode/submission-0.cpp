class Solution {
public:

    string encode(vector<string>& strs) {
        string result = "";
        for (int i = 0; i < strs.size(); i++)
            result += to_string(strs[i].length()) + '#' + strs[i];
        return result;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;
        while (i < s.length())
        {
            int j = i;
            while (s[j] != '#')
                j++;
            int length = stod(s.substr(i, j - i));
            string str = s.substr(j + 1, length);
            res.push_back(str);
            i = j + length + 1;
        }

        return res;
    }
};
