
class Solution:
    def romanToInt(self, s: str) -> int:

        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        total_sum = 0
        idx = 0

        while idx < len(s):
            if idx + 1 < len(s) and s[idx] == 'I' and s[idx + 1] == 'V':
                total_sum += 4
                idx += 2
            elif idx + 1 < len(s) and s[idx] == 'I' and s[idx + 1] == 'X':
                total_sum += 9
                idx += 2
            elif idx + 1 < len(s) and s[idx] == 'X' and s[idx + 1] == 'L':
                total_sum += 40
                idx += 2
            elif idx + 1 < len(s) and s[idx] == 'X' and s[idx + 1] == 'C':
                total_sum += 90
                idx += 2
            elif idx + 1 < len(s) and s[idx] == 'C' and s[idx + 1] == 'D':
                total_sum += 400
                idx += 2
            elif idx + 1 < len(s) and s[idx] == 'C' and s[idx + 1] == 'M':
                total_sum += 900
                idx += 2
            else:
                total_sum += roman_map[s[idx]]
                idx += 1

        return total_sum


