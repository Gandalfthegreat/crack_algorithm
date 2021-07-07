# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = []
        
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        while queue:
            pre = queue.pop(0)
            res.append(pre)
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0:
                    queue.append(cur)
        return res if len(res) == numCourses else []
