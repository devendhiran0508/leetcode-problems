int lengthOfLastWord(char* s) {
    int length = 0;
    int i = 0;
    
        while (s[i] != '\0') {
        i++;
    }
    
    while (i > 0 && s[i - 1] == ' ') {
        i--;
    }

    while (i > 0 && s[i - 1] != ' ') {
        length++;
        i--;
    }
    
    return length;
}