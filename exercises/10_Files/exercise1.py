#Using the text file student_data.dat write a program that calculates the average grade
#for each student, and print out the student's name along with their average grade.

quizzes = open('student_data.txt','r')
line = quizzes.readline()

while line: 
    values = line.split()
    average = sum(range(1,len(values))) #sum from index 1 to end of list
    print(values[0],"\t",average)
    line = quizzes.readline()

#notes
#sum will not take things like sum(1,5) or sum(1:6) or sum(2:)
    #range(1,6) gives a list. I want to sum over a list.
