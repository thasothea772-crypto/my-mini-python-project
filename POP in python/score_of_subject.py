print("======= Welcome to the grading system =======")
subject_score = [90, 90, 90, 90, 85]
python, javascript, html, cpp, php = subject_score
print("Python score    :", python)
print("Javascript score:", javascript)
print("HTML score      :", html)
print("C++ score       :", cpp)
print("PHP score       :", php)
total_score = sum(subject_score)
average_score = total_score / len(subject_score)
print("Total score     :", total_score)
print("Average score   :", average_score)

print("input your score that you got of the subjects")
int1 = input("Python score     : ")
int2 = input("Javascript score : ")
int3 = input("HTML score       : ")
int4 = input("C++ score        : ")
int5 = input("PHP score        : ")
total_score_input = int(int1) + int(int2) + int(int3) + int(int4) + int(int5)
average_score_input = total_score_input / 5
print("Total score      :", total_score_input)
print("Average score    :", average_score_input)
if average_score_input >= 50:
    print("Congratulations! You passed the exam.")
else:
    print("Sorry, you failed the exam. Better luck next time!")
    
if average_score_input >=90:
    print("Your grade = A")
elif average_score_input >=80:
    print("Your grade = B")
elif average_score_input >=70:
    print("Your grade = C")
elif average_score_input >=60:
    print("Your grade = D")
elif average_score_input >=50:
    print("Your grade = E")
else:
    print("your grade = F")
