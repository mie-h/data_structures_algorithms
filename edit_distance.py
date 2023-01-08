class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        left->right is insertion
        top->bottom is deletion
        diagonal is replacement
            r o s
          0 1 2 3
        h 1 1 2 3
        o 2 2 1 3
        r 3 2 2 2
        s 4 3 3 2
        e 5 4 4 3

        How to reconstruct a path from the 2d dp array.
        - going backward
        - if word1[i] != word2[j], find minimum from left, top, left-top.
            - if top is minimum, deletion
            - if left is minimum, insertion
            - if top-left is minimum, replacement
        - if word1[i] == word2[j], then matching.
        
        ex: [up->matching->up->matching->replacement]
        in reverse, this is replacement->deletion->deletion
        """
        
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for i in range(len(word2)+1):
            dp[0][i] = i
        for i in range(len(word1)+1):
            dp[i][0] = i
        print(dp)

        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i][j])
        print(dp)
        return dp[-1][-1]
