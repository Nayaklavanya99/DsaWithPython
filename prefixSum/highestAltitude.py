gain = [44,32,-9,52,23,-50,50,33,-84,47,-14,84,36,-62,37,81,-36,-85,-39,67,-63,64,-47,95,91,-40,65,67,92,-28,97,100,81]
# prefix = [0]* len(gain)

# prefix[1] = gain[0]
# for i in range(2,len(gain)):
#     prefix[i] = prefix[i-1] + gain[i-1]
# # prefix.insert(0,0)
# print(prefix)
# print(max(prefix))


#correct approach
cur_altitude =0 
max_altitude = 0

for i in gain:
    cur_altitude += i
    max_altitude = max(max_altitude,cur_altitude)