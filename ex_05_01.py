# ex 05 01

# enter NUMBER
nums = []
print('Please enter a number. When you are done, type \'done\' to move on.')
while True:
    user_input = input('TYPE IN A NUMBER: ')
    try:
        nums += [float(user_input)]
        print(nums)
    except ValueError:
        if str(user_input) == 'done':
            break
        else:
            print('ENTER A NUMERIC VARIABLE, or type \'done\' to move on.')
            continue

# SUM of nums
sum = 0
for i in nums:
    sum += i
# average
mean = sum / len(nums)

print('YOUR NUMBERS:', nums)
print('COUNT:', len(nums))
print('SUM:', sum)
print('AVERAGE', mean)
