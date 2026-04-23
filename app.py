from datetime import datetime, timedelta
def get_valid_date():
    while True:
        date_input=input("Enter last period date(YYYY-MM-DD):")
        try:
            return datetime.strptime(date_input,"%Y-%m-%d")
        except ValueError:
            print("Invalid Date format Try again.")
def get_valid_number(prompt):
    while True:
        value=input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print("please enter a valid number")
def save_to_file(data):
    with open("history.txt","a") as file:
        file.write(data+"\n")
def main():
    print("\n Period Tracker")
    while True:
        last_date=get_valid_date()
        cycle_length=get_valid_number("Enter Cycle length (days):")
# calculate next period
        next_period=last_date+timedelta(days=cycle_length)
# Display result
#ovulation (approx 14 days before next period)
        ovulation=next_period-timedelta(days=14)
        result= f"""
last period:{last_date.date()}
Next period:{next_period.date()}
ovulation:{ovulation.date()}
"""

        print(result)
        save_to_file(result)
        choice=input("Do you want to track again?(Y/N):").lower()
        if choice!='y':
            print("Exiting.....Stay Healthy!")
            break
if __name__=="__main__":
    main()
