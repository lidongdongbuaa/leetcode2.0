from collections import defaultdict
class Solution:
    def rankTeams(self, votes):  # return string of team name
        if len(votes) == 1:  # corner case
            return votes[0]

        num = len(votes[0])  # kinds of alphabet

        lookup = defaultdict(list)
        used = set()  # 统计出现的字符

        for vote in votes:
            for i, v in enumerate(vote):
                used.add(v)
                if len(lookup[v]) == 0:
                    lookup[v] = [0] * 26  # 构造一个dict， key是字母，value是list,[times], 元素是各个位置出现的频率
                lookup[v][i] += 1

        tmp = sorted(list(used), key = lambda x : (lookup[x], -ord(x)))  # ord 技巧
        tmp.reverse()
        return ''.join(tmp)

x = Solution()
x.rankTeams(["BCA","CAB","CBA","ABC","ACB","BAC"])