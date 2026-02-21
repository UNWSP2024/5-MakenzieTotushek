# Auther: Makenzie Totushek
# Date: 2/20/2026
# Title: Math Quiz

# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
def math_quiz(n1, n2):
    sum = n1 + n2
    return sum

def score_of_quiz(answer1):
    if answer1 == answer2:
        grade = 'Congratulations! That is correct!'
    else:
        grade = 'The correct answer is 376'
    return grade


print('What is the answer to this math equation?')
print(' 247')
print('+129')
print('-----')
answer1 = int(input('='))

answer2 = math_quiz(247, 129)

result = score_of_quiz(answer1)
print(result)