from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        total = 0
        marks_list = []

        for subject in subjects:
            marks = float(request.form[subject])
            marks_list.append(marks)
            total += marks

        average = total / len(subjects)
        grade, remark = get_grade(average)

        return render_template(
            "result.html",
            total=total,
            average=round(average, 2),
            grade=grade,
            remark=remark
        )

    return render_template("index.html", subjects=subjects)

if __name__ == "__main__":
    app.run(debug=True)