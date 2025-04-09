student_scores = [123, 463, 573, 221, 425, 246, 64, 24, 35, 67]

total_exam_score = sum(student_scores)

sum = 0
for score in student_scores:
    sum += score 

print(sum)
print(max(student_scores))

max = 0 
for score in student_scores:
    if score > max :
        max = score

print("the max score is ", max)


# Range function with for loop
sum = 0
for number in range(1, 101):
    sum +=number

print("The sum is : ", sum)
