from datetime import datetime, timedelta
last_date_input=input("Enter last period date (YYYY-MM-DD):")
cycle_length= int(input("Enter your cycle length (in days):"))
# covert string to date
last_date =datetime.strptime(last_date_input,"%Y-%m-%d")
# calculate next period
next_period=last_date+timedelta(days=cycle_length)
# Display result
#ovulation (approx 14 days before next period)
ovulation=next_period-timedelta(days=14)
print("\nNext Expected period date:",next_period.date())
print("Estimated Ovulation:",ovulation.date())
