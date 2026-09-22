# GRADES FOR STUDENTS

if False:
    score=int(input("Score: "))

    if score >= 90 and score <= 100:
        print("Grade: A")
    elif score >= 80 and score < 90:
        print("Grade: B")
    elif score >= 70 and score < 80:
        print("Grade: C")
    elif score >= 60 and score < 70:
        print("Grade: D")
    else:
        print("Grade: F")

if False:
    # Lets flip it around like a<=x<=b
    score=int(input("Score: "))
    
    if 90 <= score <= 100:
        print("Grade: A")
    elif 80 <= score < 90:
        print("Grade: B")
    elif 70 <= score < 80:
        print("Grade: C")
    elif 60 <= score < 70:
        print("Grade: D")
    else:
        print("Grade: F")

if False:
    # let's use the exclusivity of the last condition
    score=int(input("Score: "))

    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

if False:
    # Let's use a function
    # Doesn't matter what the sequence of the lines in def function is, as long as the function is defined before it is called
    def get_grade(score):
        if 90 <= score <= 100:
            return "A"
        elif 80 <= score < 90:
            return "B"
        elif 70 <= score < 80:
            return "C"
        elif 60 <= score < 70:
            return "D"
        else:
            return "F"

    score = int(input("Score: "))
    print(f"Grade: {get_grade(score)}")

if False:
    # Let's use a list
    score=int(input("Score: "))
    
    grades = [
        (90, 100, "A"),
        (80, 90, "B"),
        (70, 80, "C"),
        (60, 70, "D"),
        (0, 60, "F")
    ]
    
    for lower, upper, grade in grades:
        if lower <= score < upper:
            print(f"Grade: {grade}")
            break

if False:
    # Let's use a dictionary
    # We can use tuples as keys in a dictionary, and the values can be the grades
    score=int(input("Score: "))
    
    grades = {
        (90, 100): "A",
        (80, 90): "B",
        (70, 80): "C",
        (60, 70): "D",
        (0, 60): "F"
    }
    
    for range_, grade in grades.items():
        if range_[0] <= score < range_[1]:
            print(f"Grade: {grade}")
            break

# If you use if all the way down the mutual exclusivity will be gone