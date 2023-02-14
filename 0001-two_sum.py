#   Given an array of integers  and an integer, 
# Returns the indices of two numbers whose sum is target
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:   
                return [i, j]

#list of integers inputers
s = [int(item) for item in input("Enter the list items : ").split()]    

t = int(input("target:"))

value = two_sum(s, t)

if value:
    print(value)
else:
    print("numbers giving this target not found")


dc = {}
print(dc)
dc.setdefault(0,0)
print(dc)
