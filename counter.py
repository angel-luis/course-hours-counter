import re

with open("course.txt") as file:
    text = file.read()
    timestamps_raw = "".join(
        [m.group(1) for m in re.finditer(r".*?(\((\d+:\d+)\s*\)|$)", text)])
    timestamps = re.findall(r"\((\d+):(\d+)\s*\)", timestamps_raw)

    total_minutes = 0

    for timestamp in timestamps:
        minutes, seconds = int(timestamp[0]), int(timestamp[1])
        total_minutes += minutes + (seconds / 60)

    total_hours = total_minutes // 60
    total_minutes %= 60

    print(
        f"Total duration: {int(total_hours)} hours and {int(total_minutes)} minutes")
