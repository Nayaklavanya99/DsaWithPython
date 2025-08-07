from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()  # Initialize deque to store request timestamps
    
    def ping(self, t):
        self.queue.append(t)  # Add new request
        
        # Remove outdated requests (older than t - 3000)
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        
        return len(self.queue)  # Return count of requests in the last 3000ms

# Example Usage:
obj = RecentCounter()
print( obj.ping(1)  )  # Output: 1
print(obj.ping(100))  # Output: 2
print (obj.ping(3001)) # Output: 3
print (obj.ping(3002)) # Output: 3
