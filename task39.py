class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Remove consecutive stars
        newP = ''
        for x in range(len(p)):
            if p[x] != '*' or x == 0 or p[x-1] != '*':
                newP += p[x]
        p = newP
        m = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        # The empty string matches itself.
        m[0][0] = True
        for j in range(len(p)):
            if p[j] != '*':
                # A letter or ? won't match the empty string.
                m[0][j+1] = False
            else:
                # If star, take the previous entry.
                m[0][j+1] = m[0][j]
        for i in range(len(s)):
            # The empty pattern doesn't match any characters
            m[i+1][0] = False
        for j in range(len(p)):
            for i in range(len(s)):
                if p[j] == '*':
                    m[i+1][j+1] = m[i+1][j] or m[i][j+1]
                elif p[j] == '?':
                    m[i+1][j+1] = m[i][j]
                else:
                    m[i+1][j+1] = m[i][j] and p[j] == s[i]
        return m[len(s)][len(p)]