##aim
##bar chart and scatter plot using matplotlib
##create a list of subjects mats, physics, cs, chemistry, eng
n = int(input("choose 1 for #plot a bar chart of marks per subject \nchoose 2 for plot a scatter plot showing the relationship btw 2 random variables, study hours and marks \nchoose 3 for create marks of 5 sujects using numpy, random integers \nchoose 4 for  ##customize color, title and axis labels:"))
match n:    
    case 1:
        import matplotlib.pyplot as plt

        subjects = ["Maths", "Physics", "Chemistry", "English", "Computer Science"]
        marks = [85, 78, 92, 75, 95]

        plt.bar(subjects, marks)
        plt.xlabel("Subjects")
        plt.ylabel("Marks")
        plt.title("Marks in Different Subjects")
        plt.show()
    case 2:
        import matplotlib.pyplot as plt
        hours = [1, 2, 3, 4, 5, 6, 7, 8]
        scores = [45, 50, 55, 60, 65, 72, 80, 88]

        plt.scatter(hours, scores)
        plt.xlabel("Hours Studied")
        plt.ylabel("Exam Score")
        plt.title("Hours Studied vs Exam Score")
        plt.show()
    case 3:
        import numpy as np
        subjects = ["Maths", "Physics", "Computer Science", "English", "Chemistry"]
        marks = np.random.randint(0, 101, 5)

        print("Subjects:", subjects)
        print("Marks:", marks)
    case 4:
        import numpy as np
        import matplotlib.pyplot as plt

        subjects = ["Maths", "Physics", "Computer Science", "English", "Chemistry"]

        marks = np.random.randint(0, 101, 5)
        plt.bar(subjects, marks, color="skyblue")

        plt.title("Marks obtained in different subjects")
        plt.xlabel("subjects")
        plt.ylabel("marks")
        plt.show()

















