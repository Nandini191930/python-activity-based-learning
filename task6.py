subjects = ["Python", "Mathematics", "English"]
previous = [65, 48, 70]
latest = [78, 45, 75]
weak = []
for i in range(len(subjects)):
    change = latest[i] - previous[i]
    if change > 0:
        status = "Improved"
    elif change < 0:
        status = "Declined"
    else:
        status = "No change"
    print(subjects[i], status, "by", abs(change))
    if latest[i] < 50:
        weak.append(subjects[i])
old_avg = sum(previous) / len(previous)
new_avg = sum(latest) / len(latest)
print("Previous average:", round(old_avg, 2))
print("Latest average:", round(new_avg, 2))
if new_avg > old_avg:
    print("Overall trend: Improving")
elif new_avg < old_avg:
    print("Overall trend: Declining")
else:
    print("Overall trend: Unchanged")
print("Weak subjects:", weak)