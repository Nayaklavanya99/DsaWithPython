asteroids =[-2,-2,1,-2]
stack = []
stack.append(asteroids[0])
for i in range(1,len(asteroids)):
    if stack[-1] > 0 and asteroids[i] < 0:
        if abs(stack[-1]) == abs(asteroids[i]):
            stack.pop()
        elif abs(stack[-1]) < abs(asteroids[i]):
            stack.pop()
            i -= 1
    else:
        stack.append(asteroids[i])
print(stack)

def collisionCheck(asteroids):
    stack = []
    stack.append(asteroids[0])
    for i in range(1,len(asteroids)):
        if abs(stack[-1]) == abs(asteroids[i]):
            stack.pop()
        elif stack[-1] > 0 and asteroids[i] < 0:
            if abs(stack[-1]) < abs(asteroids[i]):
                stack.pop()
                i -= 1
        elif stack[-1] < 0 and asteroids[i] > 0:
            stack.pop()
        else:
            stack.append(asteroids[i])
    return stack

asteroid =[-2,-1,1,2]

print(collisionCheck(asteroid))

def asteroidCollision(asteroids):
        stack = []

        for asteroid in asteroids:
            # Process collisions
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(stack[-1]) < abs(asteroid):  
                    stack.pop()  # Stack asteroid is smaller, remove it
                    continue  # Recheck new stack top with the asteroid
                elif abs(stack[-1]) == abs(asteroid):  
                    stack.pop()  # Both asteroids destroy each other
                break  # Stop checking if the asteroid wasn't destroyed
            
            else:  
                stack.append(asteroid)  # Append asteroid if no collision happens

        return stack
print(asteroidCollision(asteroids))