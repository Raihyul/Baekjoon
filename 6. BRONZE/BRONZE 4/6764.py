heights = []

for _ in range(4):
    heights.append(int(input()))

if len(set(heights)) == 1:
    print("Fish At Constant Depth")
elif heights[0] - heights[1] < 0 and heights[1] - heights[2] < 0 and heights[2] - heights[3] < 0:
    print("Fish Rising")
elif heights[0] - heights[1] > 0 and heights[1] - heights[2] > 0 and heights[2] - heights[3] > 0:
    print("Fish Diving")
else:
    print("No Fish")