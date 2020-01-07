import plane
import methods
import matplotlib.pyplot as plt

nums = {}
for _ in range(10000):
    num = plane.baggage_normal()
    if num not in nums.keys():
        nums[num] = 1
    else:
        nums[num] += 1
print(nums)
keys = sorted(list(nums.keys()))
new_keys = [nums[key] for key in keys]
plt.plot(keys, new_keys)
plt.show()