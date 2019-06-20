# https://leetcode.com/problems/median-of-two-sorted-arrays/
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)

        if m == 0:
            return self.median(nums2)
        elif n == 0:
            return self.median(nums1)
        elif m == 0 and n == 0:
            return None

        if m > n:
            m, n = n, m
            nums1, nums2 = nums2, nums1

        a = self.median(nums1)
        b = self.median(nums2)

        if a == b:
            return a

        if m == n:
            if a > b:
                a, b = b,   a
                nums1, nums2 = nums2, nums1

            if m == 1:
                return (a + b) / 2.0
            if m == 2:
                return (min(nums1[1], nums2[1]) + max(nums1[0], nums2[0])) / 2.0
            if m % 2 == 0:
                return self.findMedianSortedArrays(nums1[m/2 - 1:], nums2[:m/2 + 1])
            else:
                return self.findMedianSortedArrays(nums1[m/2:], nums2[:(m/2 + 1)])

        if m == 1:
            for i in range(len(nums2)):
                if a < nums2[i]:
                    nums2.insert(i, a)
                    break
            else:
                nums2.append(a)
            return self.median(nums2)
        if m == 2:
            j = 0
            for i in range(len(nums2)):
                if nums1[j] < nums2[i]:
                    nums2.insert(i, nums1[j])
                    j = j + 1
                    if j == 2:
                        break
            else:
                nums2.append(nums1[j])
                if j == 0:
                    nums2.append(nums1[j + 1])
            return self.median(nums2)

        if a < b:
            if m % 2 == 0:
                return self.findMedianSortedArrays(nums1[m/2 - 1:], nums2[:(n - m/2 + 1)])
            else:
                return self.findMedianSortedArrays(nums1[m/2:], nums2[:(n - m/2)])
        elif a > b:
            if m % 2 == 0:
                return self.findMedianSortedArrays(nums1[:(m - m/2 + 1)], nums2[m/2 - 1:])
            else:
                return self.findMedianSortedArrays(nums1[:(m - m/2)], nums2[m/2:])

    def median(self, nums):
        n = len(nums)
        if n % 2 == 0:
            return (nums[n/2] + nums[n/2 - 1]) / 2.0
        else:
            return nums[n/2]
