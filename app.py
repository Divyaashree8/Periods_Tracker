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
def view_history():
    print("\n Cycle History")
    try:
        with open("history.txt","r") as file:
            content= file.read()
            if content.strip()=="":
                print("History is empty")
            else:
                print(content)
    except FileNotFoundError:
        print("No history found")
def clear_history():
    try:
        open("history.txt","w").close()
        print("History cleared")
    except Exception as e:
        print("Error clearing history",e)

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
        print("1.view\n2.clear History\n3.dont wanna track")
        hist= input("Choose an option:")
        if hist=="1":
            view_history()
        elif hist=="2":
            clear_history()
        elif hist=="3":
            print("Alright! Here we go.")
        choice=input("Do you want to track again?(Y/N):").lower()
        if choice!='y':
            print("Exiting.....Stay Healthy!")
            break
if __name__=="__main__":
    main()
