"""
	You have an empty sequence, and you will be given N queries. Each query is one of these three types:

	1 x  -Push the element x into the stack.
	2    -Delete the element present at the top of the stack.
	3    -Print the maximum element in the stack.
	Input Format

	The first line of input contains an integer, N. The next N lines each contain an above mentioned query. (It is guaranteed that 
	each query is valid.)

	Constraints 
	1 <= N <= 10 ^ 5
	1 <= x <= 10 ^ 9
	1 <= type <= 3
	 
	 

	Output Format

	For each type 3 query, print the maximum element in the stack on a new line.

	Sample Input

	10
	1 97
	2
	1 20
	2
	1 26
	1 20
	2
	3
	1 91
	3
	Sample Output

	26
	91

	Problem's link: https://www.hackerrank.com/challenges/maximum-element
"""

N = int(raw_input().strip())

class Stack(object):
    def __init__(self):
        self.items = []
        self.size = 0 
    def push(self, item):
        self.items.append(item)
        self.size += 1
    def pop(self):
        self.size -= 1
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def is_empty(self):
        return self.size == 0

stack = Stack()                     # each entry in the stack will store two values, current number and current max
                                    # this way we will obtain the max value in the stack in O(1) time
max_val = 0

for i in range(N):
    query = raw_input().strip().split()
    
    # push
    if query[0] == '1':
        num = int(query[1])
        max_val = max(max_val, num)
        stack.push([num, max_val])
    # pop
    elif query[0] == '2':
        if not stack.is_empty():
            stack.pop()
            if stack.size >= 1:
                max_val = stack.peek()[1]
            else:
                max_val = 0
        else:
            break 
    # print maximum element in the stack
    else:
        if not stack.is_empty():
            print stack.peek()[1]
        else:
            print 'The stack is empty'