#  Calculate Average Temperature

# numDays = int(input("How many day's temperature ?"))
# total = 0
# temp = []
# for i in range(numDays):
#     nextDay = int(input("Day" + str(i+1) + "'s high temp:"))
#     temp.append(nextDay)
#     total += temp[i]

# avg = round(total/numDays,2)
# print("\nAverage = "+ str(avg))

# above = 0
# for i in temp:
#     if i > avg:
#         above += 1
# print(str(above) + "day(s) above avarage")

#  finding the missing numbers in an integer array of 1 to 100
def missing_number(arr, n):
    # Calculate the sum of first n natural numbers
    total = n * (n+1) / 2
    # Calculate the sum of numbers in the array
    sum_arr = sum(arr)
    # Find the missing number by subtracting sum_arr from total
    missing = total - sum_arr

    return missing_number
print(missing_number([1,2,3,4,5,6],6))