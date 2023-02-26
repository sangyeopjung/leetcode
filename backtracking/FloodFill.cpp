// https://leetcode.com/problems/flood-fill/description/

class Solution {
    vector<pair<int, int>> dxdy {{0,1}, {0,-1}, {1,0}, {-1,0}};

public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        if (image[sr][sc] != color)
        {
            dfs(image, sr, sc, image[sr][sc], color);
        }
        return image;
    }

    void dfs(vector<vector<int>>& image, int sr, int sc, int from, int to)
    {
        image[sr][sc] = to;
        for (const auto& [dx, dy] : dxdy)
        {
            int x = sr + dx;
            int y = sc + dy;
            if (x >= 0 && x < image.size() && y >= 0 && y < image[0].size() 
                && image[x][y] == from)
            {
                dfs(image, x, y, from, to);
            }
        }
    }
};