# https://leetcode.com/problems/integer-to-roman/

# from collections import deque


class Solution:
    def intToRoman(self, num: int) -> str:
        def make_rome(n, symbols):
            list_ = []
            cnt = 0
            while n > cnt:
                cnt += 1
                if cnt == 4:
                    list_ = [symbols[0], symbols[1]]
                elif cnt == 5:
                    list_.pop(0)
                elif cnt == 9:
                    return "".join([symbols[0], symbols[2]])
                else:
                    list_.append(symbols[0])
            return "".join(list_)
        
        array = []
        symbol_rome = [['I', 'V', 'X'], ['X', 'L', 'C'], ['C', 'D', 'M'], ['I', 'V', 'X']]
        for i, v in enumerate(reversed(str(num))):
            if i == 3:
                array.append('M' * int(v))
            else:
                array.append(make_rome(int(v), symbol_rome[i]))
        print("".join(reversed(array)))
        return "".join(reversed(array))


a = Solution()
a.intToRoman(num=1994)