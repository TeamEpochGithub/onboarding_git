# BUGGY CODE, YOU BETTER FIX IT
# MAKE ISSUES FOR EVERY BUG AND WORK TOGETHER
# DIVIDE WORKLOAD EVENLY

class AIEngineer:
    def __init__(self, name, experience, projects):
        # Bug 1: Missing self in the constructor
        self.name = name
        self.experience = experience
        self.projects = ["project 0"]

    # Bug 3: Method not properly defined, colon missing
    def average_project_score(self)
        # Bug 4: Division by zero error if the list is empty
        return sum(self.projects) / len(self.projects)

    def add_project_score(self, score):
        # Bug 5: Function parameter not used
        self.projects.append(80)

    # Bug 6: Using single equals sign (assignment) instead of double (comparison)
    def is_promotion_due(self):
        if self.average_project_score = 85:
            return True
        else:
            return False

    # Bug 7: Method not properly defined, colon missing
    def years_to_retirement(self)
        # Bug 14: Subtracting a string from an integer
        return 65 - "self.experience"

    # Bug 8: Method with argument but no parameter
    def add_experience(years):
        self.experience += years