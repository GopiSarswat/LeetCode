class Solution {
public:
    int divide(int dividend, int divisor) {
        // Edge case: Overflow handling for -2147483648 / -1
        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }

        // Determine the sign of the final quotient
        // If one number is negative and the other is positive, result is negative
        bool isNegative = (dividend < 0) ^ (divisor < 0);

        // Convert both numbers to negative to prevent overflow when converting INT_MIN to positive
        // (INT_MIN cannot be converted to positive INT_MAX + 1 without overflowing)
        long long absDividend = abs((long long)dividend);
        long long absDivisor = abs((long long)divisor);

        long long quotient = 0;

        // Efficient repeated subtraction using bit shifting (doubling the divisor)
        while (absDividend >= absDivisor) {
            long long tempDivisor = absDivisor;
            long long multiple = 1;

            // Double the divisor until it's larger than the remaining dividend
            while (absDividend >= (tempDivisor << 1)) {
                tempDivisor <<= 1;
                multiple <<= 1;
            }

            // Subtract the largest doubled divisor found from the dividend
            absDividend -= tempDivisor;
            // Add the corresponding multiple to our quotient
            quotient += multiple;
        }

        // Apply the sign and return the result
        return isNegative ? -quotient : quotient;
    }
};
