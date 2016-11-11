import bisect
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        print(envelopes)
        dp = []
        for x in envelopes:
            i = bisect.bisect_left(dp, x[1])
            if i == len(dp):
                print(i)
                dp.append(x[1])
            else:
                dp[i] = x[1]
            print(dp)
        return len(dp)


if __name__ == '__main__':
    envels = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
    solution = Solution()
    print(solution.maxEnvelopes(envels))
