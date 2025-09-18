class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_info = {}
        self.heap = []
        for userId, taskId, priority in tasks:
            self.task_info[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, taskId))


    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_info[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))


    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId not in self.task_info:
            return
        userId, _ = self.task_info[taskId]
        self.task_info[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_info:
            del self.task_info[taskId]

    def execTop(self) -> int:
        while self.heap:
            negP, negT, tId = heapq.heappop(self.heap)
            if tId in self.task_info:
                userId, currP = self.task_info[tId]
                if currP == -negP: 
                    del self.task_info[tId]
                    return userId
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()