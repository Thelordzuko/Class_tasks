days_of_week = ("Monday", "Wednesday", "Friday")
print("Enter an activity for each of the following days:")

activities = []
for day in days_of_week:
    activity = input(f"What is your activity on {day}? ")
    activities.append(activity)
schedule = {day: activity for day, activity in zip(days_of_week, activities)}
print("\n\t--- Your Weekly Activities ---")
for day, activity in schedule.items():
    print(f"\t{day}: {activity}")