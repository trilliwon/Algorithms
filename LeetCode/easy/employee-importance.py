"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    
    def importance(self, employee, empDic):

        stack = [employee]
        imp = 0
        while len(stack) != 0:
            front = stack.pop()
            imp += front.importance

            for sub in front.subordinates:
                stack.append(empDic[sub])
        return imp

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        
        empDic = { e.id: e for e in employees }
        
        for employee in employees:
            if employee.id == id:
                return self.importance(employee, empDic)
                
        return None
        
