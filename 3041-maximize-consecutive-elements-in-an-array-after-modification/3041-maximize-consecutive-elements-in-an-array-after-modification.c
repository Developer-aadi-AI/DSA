int cmp(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

typedef struct {
    int key;
    int val;
    UT_hash_handle hh;
} HashItem;

int maxSelectedElements(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), cmp);
    
    HashItem* hash = NULL;
    int max_len = 0;
    
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        
        HashItem *item1 = NULL, *item2 = NULL;
        HASH_FIND_INT(hash, &x, item1);
        int v1 = item1 ? item1->val + 1 : 1;
        
        int prev_x = x - 1;
        HASH_FIND_INT(hash, &prev_x, item2);
        int v2 = item2 ? item2->val + 1 : 1;
        
        int key1 = x + 1;
        HashItem *target1 = NULL;
        HASH_FIND_INT(hash, &key1, target1);
        if (target1) {
            if (v1 > target1->val) target1->val = v1;
        } else {
            target1 = (HashItem*)malloc(sizeof(HashItem));
            target1->key = key1;
            target1->val = v1;
            HASH_ADD_INT(hash, key, target1);
        }
        
        int key2 = x;
        HashItem *target2 = NULL;
        HASH_FIND_INT(hash, &key2, target2);
        if (target2) {
            if (v2 > target2->val) target2->val = v2;
        } else {
            target2 = (HashItem*)malloc(sizeof(HashItem));
            target2->key = key2;
            target2->val = v2;
            HASH_ADD_INT(hash, key, target2);
        }
    }
    
    HashItem *curr, *tmp;
    HASH_ITER(hh, hash, curr, tmp) {
        if (curr->val > max_len) {
            max_len = curr->val;
        }
        HASH_DEL(hash, curr);
        free(curr);
    }
    
    return max_len;
}