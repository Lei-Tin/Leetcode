/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findThePrefixCommonArray(int* A, int ASize, int* B, int BSize, int* returnSize) {
    int *ans = malloc(sizeof(int) * ASize);

    int freq[50] = {0};

    for (int i = 0; i < ASize; ++i) {
        ++freq[A[i] - 1];
        ++freq[B[i] - 1];

        int cnt = 0;

        for (int j = 0; j < 50; ++j) {
            cnt += freq[j] == 2 ? 1 : 0;
        }

        ans[i] = cnt;
    }

    *returnSize = ASize;

    return ans;
}