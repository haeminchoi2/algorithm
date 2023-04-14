# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        array = [[] for _ in range(numRows)]
        cnt = 0
        flag = True
        for string in s:
            array[cnt].append(string)
            if flag:
                cnt += 1
            else:
                cnt -= 1

            if cnt == numRows - 1:
                flag = False
            elif cnt == 0:
                flag = True
        answer = ""
        for l in array:
            answer += "".join(l)
        return answer

a = Solution()
a.convert(s = "abc", numRows = 1)