#Find the sum of integer value
student_score=[85, 92, 78, 88, 95]
total_exam_score = sum(student_score)
print(f"Total exam score:{total_exam_score}")
sum=0
for score in student_score:
    sum+=score
print(f"Total score: {sum}")

#Find the maximum integer value
print(max(student_score))
max=student_score[0]
for score in student_score:
    if score > max:
        max = score
print(f"Maximum score: {max}")

#Range intro
for num in range(1,10,3):
 print(num)

#Gauss problem
total=0
for num1 in range(1,101):
    total+=num1
print(f"Sum of numbers from 1 to 100: {total}") 