class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        if denominator == 0:
            return ''
        result = ''
        # -ve case
        if (numerator < 0) ^ (denominator < 0):
            result += '-'
        numerator, denominator = abs(numerator), abs(denominator)

        quotient, remainder = divmod(numerator, denominator)
        result += str(quotient)
        if not remainder:
            return result
        result += '.'

        remainder_dict = {}
        while remainder and remainder not in remainder_dict:
            remainder_dict[remainder] = len(result)
            remainder *= 10
            result += str(remainder // denominator)
            remainder %= denominator
        # Repeat check
        if remainder in remainder_dict:
            result = result[:remainder_dict[remainder]] + '(' + result[remainder_dict[remainder]:] + ')'
        return result


s = Solution()
# print(s.fractionToDecimal(1, 2))
# print(s.fractionToDecimal(2, 1))
print(s.fractionToDecimal(-50, 8))
