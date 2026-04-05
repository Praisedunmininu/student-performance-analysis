📊 Student Performance Analysis

🧾 Introduction
This project focuses on analyzing student performance using data analysis techniques in Python. 
The aim is to identify the key factors that influence academic success and understand patterns within the dataset.

🎯 Objective
The main objective of this analysis is to:
Examine the relationship between study habits and academic performance
Identify the most important factors affecting student scores
Compare high-performing and low-performing students


## Dataset Note
 The full dataset is large and not included in this repository.  
A sample dataset (student_performance_sample.csv) is provided for demonstration purposes



📂 Dataset Description
The dataset contains the following variables:
student_id – Unique identifier for each student
weekly_self_study_hours – Number of hours spent studying weekly
attendance_percentage – Student attendance rate
class_participation – Level of participation in class (scale)
total_score – Overall academic score
grade – Final grade (A–F)

🔍 Exploratory Data Analysis (EDA)
Initial exploration of the dataset shows:
A large number of students achieved high scores
The average score is relatively high
Grade “A” appears most frequently
This raises questions about whether the dataset reflects real-world behavior or is simulated.

📊 Correlation Analysis
To understand relationships between variables, correlation analysis was performed.

Key Results:
Weekly self-study hours vs total score: Strong positive correlation (≈ 0.82)
Attendance vs total score: No meaningful correlation (≈ 0)
Class participation vs total score: No meaningful correlation (≈ 0)

Interpretation:
Weekly self-study hours is the strongest predictor of student performance.

🥇 High-Performing Students

Students with the highest scores (close to 100):
-Typically studied more than 15 hours per week
-Had generally good attendance
-Showed varying levels of class participation

Insight:
Even students with lower participation still performed well if their study hours were high.

⚠️ Low-Performing Students

-Students with low scores:
=Had very low or zero study hours
-Sometimes had good attendance
-Showed inconsistent participation

Insight:
Attendance alone does not guarantee good performance without sufficient study time.

💡 Key Findings

-Study hours have the strongest impact on performance
-Attendance and participation have minimal influence in this dataset
-High study effort leads to high academic success
-Low study effort leads to poor performance regardless of attendance

🧠 Critical Observation

The dataset may be simulated because:
-A very large number of students achieved high grades
-Attendance and participation show no real impact on performance
-Real-world data typically shows more balanced relationships

🚀 Conclusion

Students who dedicate more time to self-study are significantly more likely to achieve high academic performance. 
While attendance and participation may support learning, they do not independently determine success.

🛠 Tools Used
Python
Pandas
NumPy
Matplotlib

✍️ Author
Islamiat Seriki
