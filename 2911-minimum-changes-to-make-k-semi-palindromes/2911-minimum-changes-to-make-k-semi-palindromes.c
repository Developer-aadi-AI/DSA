#define INF 1000000000

int minimumChanges(char* s, int k) {
    int n = strlen(s);

    int** divisors = malloc((n + 1) * sizeof(int*));
    int* divCount = calloc(n + 1, sizeof(int));

    for (int d = 0; d <= n; d++) {
        divisors[d] = malloc((n + 1) * sizeof(int));
    }

    for (int d = 1; d <= n; d++) {
        for (int v = 1; v < d; v++) {
            if (d % v == 0) {
                divisors[d][divCount[d]++] = v;
            }
        }
    }

    int** cost = malloc((n + 1) * sizeof(int*));

    for (int i = 0; i <= n; i++) {
        cost[i] = malloc((n + 1) * sizeof(int));

        for (int j = 0; j <= n; j++) {
            cost[i][j] = INF;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int L = j - i + 1;
            int best = INF;

            for (int idx = 0; idx < divCount[L]; idx++) {
                int d = divisors[L][idx];
                int changes = 0;

                for (int start = i; start < i + d; start++) {
                    int l = start;
                    int r = start + ((j - start) / d) * d;

                    while (l < r) {
                        if (s[l] != s[r]) {
                            changes++;
                        }

                        l += d;
                        r -= d;
                    }
                }

                if (changes < best) {
                    best = changes;
                }
            }

            cost[i][j] = best;
        }
    }

    int** dp = malloc((k + 1) * sizeof(int*));

    for (int t = 0; t <= k; t++) {
        dp[t] = malloc((n + 1) * sizeof(int));

        for (int i = 0; i <= n; i++) {
            dp[t][i] = INF;
        }
    }

    dp[0][0] = 0;

    for (int t = 1; t <= k; t++) {
        for (int i = t; i <= n; i++) {
            for (int j = t - 1; j < i; j++) {
                if (dp[t - 1][j] < INF &&
                    cost[j][i - 1] < INF) {

                    int candidate =
                        dp[t - 1][j] + cost[j][i - 1];

                    if (candidate < dp[t][i]) {
                        dp[t][i] = candidate;
                    }
                }
            }
        }
    }

    int result = dp[k][n];

    for (int d = 0; d <= n; d++) {
        free(divisors[d]);
    }
    free(divisors);
    free(divCount);

    for (int i = 0; i <= n; i++) {
        free(cost[i]);
    }
    free(cost);

    for (int t = 0; t <= k; t++) {
        free(dp[t]);
    }
    free(dp);

    return result;
}