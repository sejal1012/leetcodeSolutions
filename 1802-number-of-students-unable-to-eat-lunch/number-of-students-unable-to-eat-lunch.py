from collections import deque
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        studentsqueue = deque(students)
        for sandwiche in sandwiches:
            receivedSandwich = False
            count = 0
            while(not (receivedSandwich or count > len(studentsqueue))):
                # print(studentsqueue, count, sandwiche, "start")
                if(studentsqueue[0] == sandwiche):
                    studentsqueue.popleft()
                    receivedSandwich = True
                else:
                    gobackStudent = studentsqueue.popleft()
                    studentsqueue.append(gobackStudent)
                    count += 1
                    print(count, "count")
                # print(studentsqueue, count, sandwiche, "finish")
            if(count > len(studentsqueue)):
                break
        # print(studentsqueue, "here")
        return len(studentsqueue)