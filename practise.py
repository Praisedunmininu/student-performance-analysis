# =============================
# 🌹1. Import Libraries
# ==============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==============================
# 🌹2. Load Dataset
# ===============================
df = pd.read_csv(r"C:\Users\Islamiat Seriki\Applications_Falls 2026\student score\student_performance.csv")

# ================================
#🌹3. Preview Data
print(df.head())

# ====================
# 🌹4. Basic Dataset Information
# ===============================
print(df.columns)
print(df.shape)
print(df.info())

# =========================
# 🌹5. Missing Values Check
# =========================
print(df.isnull().sum())

# ==========================
# 🌹6. Full statistical Summary
#     (incuding categorical data)
# ==============================
print(df.describe(include="all"))

# ================================
# 🌹Basic stastistics (Total_score)
# ================================
print(df["total_score"].median())
print(df["total_score"].mean())

# ==============================
# 🌹Average Score by Grade
# ===============================
print(df.groupby("grade")["total_score"].mean())

# ==================================
# 🌹 Pass vrs Fail Analysis
# =======================================
student_passed = df[df["total_score"]>=50].shape[0]
print("Passed student:",student_passed)

student_failed = df[df["total_score"]<50].shape[0]
print("Failed_student:",student_failed)

# =============================
# 🌹Categorize Student Scores
# ===============================
bins = [0,60,84,100]
labels = ["low","average","high"]

df["student_score"] = pd.cut(
    df["total_score"],
    bins=bins,
    labels=labels
)
print(df[["total_score","student_score"]].head())
print(df["student_score"].value_counts())

# ===============================
# 🌹 Identify Good Students
# ================================
good_score =df[
    (df["total_score"]>=80)&
    (df["attendance_percentage"]>70)
]
print(good_score.shape)
print(good_score.head())
# =============================
# 🌹High Score but Low Study
# =============================
high_score_low_study= df[
    (df["total_score"]>=90)&
    (df["weekly_self_study_hours"]<10)
]
print(high_score_low_study.shape)
print(high_score_low_study.head())

# ==========================
# 🌹Correlation Analysis
# =============================
print(df["weekly_self_study_hours"].corr(df["total_score"]))
print(df["attendance_percentage"].corr(df["total_score"]))

# =============================
# 🌹 Group Analysis by Grade
# =====================================
more_hours = df.groupby("grade")["weekly_self_study_hours"].mean().reset_index()
print(more_hours)

highest_score = df.groupby("grade")["total_score"].mean().reset_index()
print(highest_score)

attendance = df.groupby("grade")["attendance_percentage"].mean().reset_index
print(attendance)

# ===================================
# 🌹 Hardworking Student Analysis
# =========================================

hard_working = df[
    (df["weekly_self_study_hours"]>15)
].groupby("grade").size().reset_index(name="hardworking_count")

print(hard_working)

hard_working_student = df[
    (df["weekly_self_study_hours"]>15)
].groupby("grade")["total_score"].mean().reset_index()

print(hard_working_student)

# ======================================
# 🌹High Attendance & Top Student %
# =========================================

high_attendance = df[df["attendance_percentage"]>80]
top_students = high_attendance[high_attendance["total_score"]>90]

total_students = high_attendance.shape[0]
top_count = top_students.shape[0]

percentage = top_count/total_students*100
print(percentage)

# ===================================
# 🌹Study Hard + Attendance %
# =========================================

study_hard = df[(df["weekly_self_study_hours"]>15)]
big_attendance = study_hard[study_hard["attendance_percentage"]>85]

total_students = study_hard.shape[0]
top_count = big_attendance.shape[0]

percentage =(top_count/total_students)*100
print(percentage)

# =======================================
# 🌹 Factor Influencing Performance
# ========================================

print(df["weekly_self_study_hours"].corr(df["total_score"]))
print(df["attendance_percentage"].corr(df["total_score"]))
print(df["class_participation"].corr(df["total_score"]))

# =====================================
# 🌹Scatter Plot (Study Hours vs Score)
# ========================================

x=df["weekly_self_study_hours"]
y=df["total_score"]

plt.scatter(x,y)
plt.title("student_performance")
plt.xlabel("weekly_self_study_hours")
plt.ylabel("total_score")
plt.show()

# =====================================
# 🌹Histogram (Score Distribution)
# =====================================

plt.hist(df["total_score"],bins=10)
plt.title("student_performance")
plt.xlabel("total_score")
plt.ylabel("number of student")
plt.show()
plt.close()

# ==============================
#🌹Study Hours by Grade (Bar Chart)
# =====================================

hard_study = df.groupby("grade")["weekly_self_study_hours"].mean().reset_index()

x= hard_study["grade"]
y = hard_study["weekly_self_study_hours"]

plt.bar(x,y)
plt.title("Average study hours by grade")
plt.xlabel("Grade")
plt.ylabel("Study hours")
plt.show()
plt.close()

# =================================
#🌹Attendance vs Score Scatter
# ================================

x = df["attendance_percentage"]
y= df["total_score"]

plt.scatter(x,y)
plt.title("good student")
plt.xlabel("attendance_percentage")
plt.ylabel("total_store")
plt.show()
plt.close()

# ================================
# 🌹Advance Scatter Plot (Multi-variable)
# ======================================
x = df["weekly_self_study_hours"]
y = df["total_score"]

plt.scatter(x,y,
c=df["attendance_percentage"],
s=df["class_participation"],
alpha=0.05)

plt.xlabel("weekly_self_study_hours")
plt.ylabel("total_score")
plt.show()
plt.close()

# ===============================
# 🌹Top & Lowest score
# =====================================

highest_score = df.sort_values("total_score",ascending=False).head(10)
print(highest_score)

lowest_score = df.sort_values("total_score",ascending=True).head(10)
print(lowest_score)

# ===================================
# 🌹Hard Study but Low Score %
# ===================================

study_hard = df[df["weekly_self_study_hours"]>15]  
low_score = study_hard[study_hard["total_score"]<60]

total_student = study_hard.shape[0] 
low_student = low_score.shape[0] 

percentage = (low_student/total_student)*100
print(percentage) 

# =====================================
# 🌹 Low Study but High Score
# ======================================

low_study_high_score = df[
    (df["weekly_self_study_hours"]<5)&
    (df["total_score"]>90) 
]
print(low_study_high_score.shape[0])   

# =================================
# 🌹Low Attendance but High Score
# =======================================


students = df[
    (df["attendance_percentage"]<60)&
    (df["total_score"]>85)
]
print(students)

# =====================================
# 🌹 Boxplot (Score Distribution by Grade)
# =========================================

plt.boxplot([
df[df["grade"]=="A"]["total_score"],
df[df["grade"]=="B"]["total_score"],
df[df["grade"]=="C"]["total_score"],
df[df["grade"]=="D"]["total_score"]
])
plt.xticks([1,2,3,4],
["A","B","C","D"])   
plt.title("Distribution of student total score by grade")   
plt.ylabel("total_score")
plt.show()
plt.close()

    


