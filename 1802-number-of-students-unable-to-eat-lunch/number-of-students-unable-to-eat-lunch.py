from collections import deque
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        studentsqueue = deque(students)
        countSandwich = [0,0]
        for student in students:
            countSandwich[student] += 1
        for sandwiche in sandwiches:
            receivedSandwich = False
            if(countSandwich[sandwiche] == 0):
                break
            while(not (receivedSandwich)):
                if(countSandwich[sandwiche] == 0):
                    break
                if(studentsqueue[0] == sandwiche):
                    studentsqueue.popleft()
                    receivedSandwich = True
                    countSandwich[sandwiche] -= 1
                else:
                    gobackStudent = studentsqueue.popleft()
                    studentsqueue.append(gobackStudent)
        return len(studentsqueue)