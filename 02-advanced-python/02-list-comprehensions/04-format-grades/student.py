# Write your code here
def format_grades(grades):
    def avg(xs):
        return round(sum(xs) / len(xs))
    return "\n".join(f'{name}: {avg(grade)}' for name, grade in grades.items())