n = int(input("Enter the n: "))
count_fail = 0
count_valid = 0
marks = [0]*n
for i in range(n):
    marks[i] = int(input("Enter the marks: "))
print("Input marks:",marks)
print("Output:")
for k in range(n):
    if marks[k] < 0 or marks[k] > 100:
        print(f"{marks[k]}-->Invalid")

    elif marks[k] >= 90 and marks[k] <= 100:
        print(f"{marks[k]}-->Excellent")
        count_valid += 1
    elif marks[k] >= 75 and marks[k] <= 89:
        print(f"{marks[k]}-->Very Good")
        count_valid += 1
    elif marks[k] >= 60 and marks[k] <= 74:
        print(f"{marks[k]}-->Good")
        count_valid += 1
    elif marks[k] >= 40 and marks[k] <= 59:
        print(f"{marks[k]}-->Average")
        count_valid += 1
    else:
        print(f"{marks[k]}-->Fail")
        count_fail += 1

print("Total Valid Students:",count_valid)
print("Total Failed Students:",count_fail)


