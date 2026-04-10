subjects = ["Math", "Science", "English", "History", "Computer Science"]

def get_grade(avg):
    if avg >= 90:
        return "A+", "Outstanding"
    elif avg >= 80:
        return "A", "Excellent"
    elif avg >= 70:
        return "B", "Good"
    elif avg >= 60:
        return "C", "Average"
    elif avg >= 50:
        return "D", "Needs Improvement"
    else:
        return "F", "Fail"

def main():
    total = 0

    print("🎓 Student Grade Calculator")
    print("-" * 30)

    for subject in subjects:
        while True:
            try:
                marks = float(input(f"Enter marks for {subject}: "))
                if 0 <= marks <= 100:
                    total += marks
                    break
                else:
                    print("❌ Marks must be between 0 and 100.")
            except ValueError:
                print("❌ Invalid input! Please enter a number.")

    average = total / len(subjects)
    grade, remark = get_grade(average)

    print("\n📊 Final Result")
    print("-" * 30)
    print("Total Marks:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("Remark:", remark)

if __name__ == "__main__":
    main()