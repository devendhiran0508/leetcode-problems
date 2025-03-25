int romanToInt(char* s) {
    int total = 0;
    int prevValue = 0;

    while (*s) {
        int currentValue;

        switch (*s) {
            case 'I': currentValue = 1; break;
            case 'V': currentValue = 5; break;
            case 'X': currentValue = 10; break;
            case 'L': currentValue = 50; break;
            case 'C': currentValue = 100; break;
            case 'D': currentValue = 500; break;
            case 'M': currentValue = 1000; break;
            default: return -1; // Invalid Roman numeral
        }

        if (currentValue > prevValue) {
            total += currentValue - 2 * prevValue;
        } else {
            total += currentValue;
        }

        prevValue = currentValue;
        s++;
    }

    return total;
}