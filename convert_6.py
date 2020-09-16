"""
6. Z 字形变换
难度 中等
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R    # 0, 4 (2n-2), 8 (4n-4) , 12 (6n-6)
E T O E S I I G  # 1,3,5,7,9,11
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);
示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
L   C   I   R
E T O E S I I G
E   D   H   N
示例 2
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:
L     D     R
E   O E   I I
E C   I H   N
T     S     G

PAYPALISHIRING 3
P   A   H   N
A P L S I I G
Y   I   R

P     I     N
A   L S   I G
Y A   H R
P     I
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """二维数组"""
        if numRows == 1:
            return s
        if numRows >= len(s):
            return s
        rows = []
        n = min(len(s), numRows)
        for i in range(n):
            rows.append([])
        going_down = True
        cur_row = 0
        for c in s:
            rows[cur_row].append(c)
            if going_down:
                cur_row += 1
                if cur_row == n - 1:
                    going_down = False
            else:
                cur_row -= 1
                if cur_row == 0:
                    going_down = True
        ret = ''
        for row in rows:
            for c in row:
                ret += c
        return ret


so = Solution()
for s, rows, res in [
    ['LEETCODEISHIRING', 3, 'LCIRETOESIIGEDHN'],
    ['LEETCODEISHIRING', 4, 'LDREOEIIECIHNTSG'],
    ['PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'],
    ['PAYPALISHIRING', 4, 'PINALSIGYAHRPI'],
    ['A', 2, 'A'],
    ['ABCDE', 4, 'ABCED'],
    ['AB', 1, 'AB']
]:
    result = so.convert(s, rows)
    print(result)
    assert result == res
