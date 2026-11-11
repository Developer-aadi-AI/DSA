long long minimumCost(int cost1, int cost2, int costBoth,
                      int need1, int need2) {
    long long mini = need1 < need2 ? need1 : need2;

    int minimum = costBoth < cost1 + cost2
                ? costBoth
                : cost1 + cost2;

    long long ans = 1LL * minimum * mini;

    long long rem1 = need1 - mini;
    long long rem2 = need2 - mini;

    if(rem1 > 0) {
        int unitCost = costBoth < cost1 ? costBoth : cost1;
        ans += 1LL * unitCost * rem1;
    }

    if(rem2 > 0) {
        int unitCost = costBoth < cost2 ? costBoth : cost2;
        ans += 1LL * unitCost * rem2;
    }

    return ans;
}