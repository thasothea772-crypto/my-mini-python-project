# test numpy part 5: Boolean Indexing
import numpy as np

student_scores = np.array([40, 50, 45, 35, 60, 20, 90, 90, 80, 70, 95, 85])
student_scores.sort()

# if student have scores >= 50, so they pass the exam.
pass_student = student_scores[student_scores >= 50]
print(f"Pass Student: {pass_student}")

# if student have scores <= 49, their score are 0, so they fied the exam.
fied_student = (student_scores[student_scores <= 49])
print(f"Fied Student: {fied_student}")