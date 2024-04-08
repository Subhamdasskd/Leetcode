class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        N = len(sandwiches)

        z = students.count(0)
        o = students.count(1)

        for index, s in enumerate(sandwiches):
            if s == 1 and o > 0:
                o -= 1
                continue
            elif s == 0 and z > 0:
                z -= 1
                continue
            else:
                return N - index
        return