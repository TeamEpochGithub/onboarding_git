# main.py
import ai_engineer

engineer = ai_engineer.AIEngineer("Jane Doe", 5, [85, 88, 90])

print(engineer.name)

average = engineer.average_project_score()

print("Average project score:", average)

# Bug 11: Trying to add a string instead of a project score (integer)
engineer.add_project_score("Excellent")

print("Project scores after adding a new score:", engineer.projects)

# Bug 12: Comparison operator used instead of assignment operator
promotion_due = engineer.is_promotion_due = True

print("Is a promotion due?:", promotion_due)
