# maps

```python
# 1. Initialize the dictionary with numeric keys and values
# Key: Student ID (int) -> Value: Exam Score (int)
scores = {101: 85, 102: 92}
print("Initial scores:", scores)



# 2. Use .get() to read a score safely
# Student 103 hasn't taken the test yet, so we return a default score of 0.
student_103_score = scores.get(103, 0)
print(f"\n[get] Student 103 score: {student_103_score}")



# 3. Use [] assignment to add or change a score
scores[103] = 78 # Adds a new student ID and score
scores[101] = 88 # Updates Student 101's score after a regrade
print("\n[[] assignment] Added student 103 and updated 101:")
print(scores)



# 4. Use .update() to process multiple scores at once
# We process a batch of new test submissions.
batch_scores = {104: 95, 105: 81, 102: 96}
scores.update(batch_scores)
print("\n[.update()] Processed a batch of new scores:")
print(scores)

scores = {101: 88, 102: 96, 103: 78}


for student_id, score in scores.items():
    print(f"Student ID {student_id} earned a score of {score}")


for student_id in scores.keys():
    print(f"Present Student ID: {student_id}")


for score in scores.values():
    print(f"Value: {score}")
```
