import datetime
import os

FILE_NAME = "study_data.txt"

def get_today():
    return str(datetime.date.today())

def read_data():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
    
    data = []
    for line in lines:
        date, hours = line.strip().split(",")
        data.append((date, float(hours)))
    return data

def write_data(date, hours):
    with open(FILE_NAME, "a") as f:
        f.write(f"{date},{hours}\n")

def calculate_streak(data):
    if not data:
        return 0
    
    streak = 0
    today = datetime.date.today()
    
    for i in range(len(data)-1, -1, -1):
        date_str, _ = data[i]
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        
        if date_obj == today - datetime.timedelta(days=streak):
            streak += 1
        else:
            break
    
    return streak

def get_level(hours):
    if hours <= 2:
        return "📘 Beginner"
    elif 3 <= hours <= 5:
        return "🔥 Focused"
    else:
        return "💀 Beast Mode"

def weekly_summary(data):
    today = datetime.date.today()
    week_ago = today - datetime.timedelta(days=7)
    
    total = 0
    days = 0
    
    for date_str, hours in data:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        if date_obj >= week_ago:
            total += hours
            days += 1
    
    return total, days

def motivation(hours):
    if hours == 0:
        return "Start small. Even 30 minutes matters!"
    elif hours < 3:
        return "Good start! Keep pushing 💪"
    elif hours < 6:
        return "You're doing great! Stay consistent 🔥"
    else:
        return "Insane focus today! Future topper energy 💯"

def main():
    print("===== STUDY STREAK TRACKER =====")
    
    today = get_today()
    data = read_data()
    
    # Check if already entered today
    for date, _ in data:
        if date == today:
            print("You already logged study hours today.")
            break
    else:
        try:
            hours = float(input("Enter study hours for today: "))
            write_data(today, hours)
            print("Saved successfully!")
            print("Level:", get_level(hours))
            print(motivation(hours))
        except:
            print("Invalid input!")
            return
    
    data = read_data()
    streak = calculate_streak(data)
    total_week, days_week = weekly_summary(data)
    
    print("\n🔥 Current Study Streak:", streak, "day(s)")
    print("📊 Weekly Study Total:", total_week, "hours in", days_week, "day(s)")
    print("Keep grinding! 🚀")

if __name__ == "__main__":
    main()