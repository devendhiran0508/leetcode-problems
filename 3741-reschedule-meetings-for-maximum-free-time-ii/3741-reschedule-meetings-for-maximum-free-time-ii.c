int maxFreeTime(int eventTime, int* startTime, int startTimeSize, int* endTime, int endTimeSize) {
    int n = startTimeSize;
    bool* q = (bool*)calloc(n, sizeof(bool));
    int t1 = 0, t2 = 0;
    for (int i = 0; i < n; i++) {
        if (endTime[i] - startTime[i] <= t1) {
            q[i] = true;
        }
        t1 = fmax(t1, startTime[i] - (i == 0 ? 0 : endTime[i - 1]));

        if (endTime[n - i - 1] - startTime[n - i - 1] <= t2) {
            q[n - i - 1] = true;
        }
        t2 = fmax(t2,
                  (i == 0 ? eventTime : startTime[n - i]) - endTime[n - i - 1]);
    }

    int res = 0;
    for (int i = 0; i < n; i++) {
        int left = i == 0 ? 0 : endTime[i - 1];
        int right = i == n - 1 ? eventTime : startTime[i + 1];
        if (q[i]) {
            res = fmax(res, right - left);
        } else {
            res = fmax(res, right - left - (endTime[i] - startTime[i]));
        }
    }
    free(q);
    return res;
}