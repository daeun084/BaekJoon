from collections import deque

def solution(operations):
    queue = deque()
    
    for operation in operations:
        op = operation.split()
        
        if op[0] == "I":
            queue.append(int(op[1]))
            queue = deque(sorted(queue))
        elif op[0] == "D":
            if (int(op[1]) < 0):
                # pop min value
                if queue:
                    queue.popleft()
            else:
                # pop max value
                if queue:
                    queue.pop()
    
    if not queue:
        return [0, 0]
    else:
        return [queue[len(queue) - 1], queue[0]]