int divide(int dividend, int divisor) {
    if (dividend == INT_MIN && divisor == -1)
        return INT_MAX;

    if (divisor == 0)
        return 0;
    else
        return dividend / divisor;
}
