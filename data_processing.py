from pyspark.sql import SparkSession
import pandas as pd
import random
spark = SparkSession.builder.appName("ResultManagementSystem").getOrCreate()
subjects = ["Electronics", "Programming", "Database", "Data Science", "Mathematics", "DSA"]
def generate_student_profiles(num_students=10000):
    return [f'Student{i}' for i in range(num_students)]
def generate_marks(num_students=10000, subjects=subjects):
    marks = {subject: [random.randint(0, 100) for _ in range(num_students)] for subject in subjects}
    return pd.DataFrame(marks)
students = generate_student_profiles()
marks_df = generate_marks(len(students))
marks_df['Student Name'] = students
spark_df = spark.createDataFrame(marks_df)
marks_df.to_csv("student_results.csv", index=False)
