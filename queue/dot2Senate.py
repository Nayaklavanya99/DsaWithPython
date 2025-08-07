senate = "DDRRR"

# queue = []
# queue.append(senate[0])


# for i in range(1, len(senate)-1):
#     if queue[0] != senate[i]:
#         if senate[i+1] == queue[0]:
#             continue
#         else:
#             queue.pop(0)
#             queue.append(senate[i])
# ans = "".join(queue)
# if ans == "R":
#     print("Radiant")
# elif ans == "D":
#     print("Dire")


from collections import deque
def predictPartyVictory(senate) :
        radiant = deque()
        dire = deque()
        
        # Step 1: Store the indices of 'R' and 'D' in separate queues
        n = len(senate)
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        print(radiant)
        print(dire)
        # Step 2: Process the bans in rounds
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            print(r,"===",d)
            
            # The senator that appears earlier bans the opponent
            if r < d:
                radiant.append(r + n)  # Radiant wins, re-enter in the next round
                print('now; ',radiant)
            else:
                dire.append(d + n) # Dire wins, re-enter in the next round
                print('now; ',dire)

        # Step 3: Determine the winner
        return "Radiant" if radiant else "Dire"
    
print(predictPartyVictory(senate))  # Output: "Radiant"
