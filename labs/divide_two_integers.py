class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # weird behaviour, tests not passed without it
        # calculator returns 2147483648, but leetcode tests not
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        precision = 0.5
        sign = -1 if (dividend > 0) != (divisor > 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)

        left = 0
        right = dividend * 2

        while True:
            mid = left + (right - left) / 2

            if abs(divisor * mid - dividend) <= precision:
                return int(mid * sign)

            if divisor * mid < dividend:
                left = mid
            else:
                right = mid
