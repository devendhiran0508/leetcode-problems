class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        m=len(workers)
        n=len(tasks)
        tasks.sort()
        workers.sort()

        def check(mid:int)->bool:
            p=pills
            worker_set=SortedList(workers[m-mid:])
            for i in range(mid-1,-1,-1):
                if worker_set[-1]>=tasks[i]:
                    worker_set.pop()
                else:
                    if p==0:
                        return False
                    r=worker_set.bisect_left(tasks[i]-strength)
                    if r==len(worker_set):
                        return False
                    p-=1
                    worker_set.pop(r)
            return True
        left=1
        right=min(m,n)
        result=0
        while left<=right:
            mid=(left+right)//2
            if check(mid):
                result=mid
                left=mid+1
            else:
                right=mid-1
        return result