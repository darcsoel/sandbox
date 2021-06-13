class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
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
