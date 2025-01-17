class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0 and nums:
            return 1

        # Sliding window
        i, j = 0, 0

        buckets = [0 for _ in range(32)]

        def get_val(b):
            ret = 0
            for i in range(32):
                ret += 1 << i if buckets[i] else 0

            return ret

        def modify_bucket(b, val, add):
            for i in range(32):
                if (val >> i) & 1 == 1:
                    if add:
                        b[i] += 1
                    else:
                        b[i] -= 1

        ans = float('inf')
        n = len(nums)

        while i < n and j < n:
            if get_val(buckets) < k:
                # Add j
                modify_bucket(buckets, nums[j], True)
                j += 1
            else:
                # Remove i
                modify_bucket(buckets, nums[i], False)
                i += 1

                if i > j:
                    j = i + 1

            if get_val(buckets) >= k:
                ans = min(ans, j - i)

        if j == n:
            # Try to shrink left as much as possible
            while i < n and i < j and get_val(buckets) >= k:
                # Remove i
                modify_bucket(buckets, nums[i], False)
                i += 1

                if get_val(buckets) >= k:
                    ans = min(ans, j - i)

        return -1 if ans == float('inf') else ans