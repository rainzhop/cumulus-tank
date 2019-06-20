# https://leetcode.com/problems/climbing-stairs/
#
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        waysCnt = 0
        maxTwoCnt = n/2
        fac = [1] * (n + 1)
        for i in xrange(1, n + 1):
            fac[i] = i * fac[i - 1]
        print fac
        for twoCnt in xrange(0, maxTwoCnt + 1):
            oneCnt = n - twoCnt
            waysCnt += fac(n) / (fac(twoCnt) * fac(oneCnt))
        return waysCnt
