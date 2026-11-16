#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char* digitSum(char* s, int k) {
    char* current = malloc(strlen(s) + 1);
    strcpy(current, s);

    while(strlen(current) > k) {
        int n = strlen(current);
        int groups = (n + k - 1) / k;

        char temp[20];
        int max_digits = sprintf(temp, "%d", 9 * k);

        char* new_s = malloc(groups * max_digits + 1);
        int pos = 0;

        for(int i = 0; i < n; i += k) {
            int ans = 0;

            for(int j = i; j < i + k && j < n; j++)
                ans += current[j] - '0';

            pos += sprintf(new_s + pos, "%d", ans);
        }

        new_s[pos] = '\0';

        free(current);
        current = new_s;
    }

    return current;
}