class Solution:
    def minMeetingRooms(self, intervals) -> int:  # input[[]], find min rooms we need
        if intervals == []:  # edge case
            return 0
        if len(intervals) == 1:  # edge case
            return 1

        intervals.sort(key=lambda x: x[0])  # sort the intervals based on first value of elements

        stack = []
        stack.append(intervals[0][1])
        tmp = []
        output = 0
        for i in range(1, len(intervals)):  # find the min number of rooms
            for j in range(len(stack)):
                if stack[j] > intervals[i][0]:
                    tmp.append(stack[j])
            tmp.append(intervals[i][1])
            stack = tmp
            output = max(output, len(stack))
            tmp = []
        return output

x = Solution()
x.minMeetingRooms([[1, 5], [8, 9], [8, 9]])