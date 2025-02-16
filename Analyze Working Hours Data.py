import pandas as pd

# Load the Excel file
file = r"C:\Users\Vamshi Yempally\Downloads\Date_workinghours.xlsx"
df = pd.read_excel(file)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%b')  # Abbreviated month (Jan, Feb, ...)
df['Weekday'] = df['Date'].dt.strftime('%A')  # Full weekday name

# Calculate overall averages
avg_tos = df['TOS'].mean()
avg_ptos = df['PTOS'].mean()

# Calculate monthly averages
monthly_avg = df.groupby('Month')[['TOS', 'PTOS']].mean().rename(columns={'TOS': 'Worked Hours', 'PTOS': 'Productive Hours'})

# Calculate weekday averages
weekday_avg = df.groupby('Weekday')[['TOS', 'PTOS']].mean().rename(columns={'TOS': 'Worked Hours', 'PTOS': 'Productive Hours'})

# Find the highest and lowest productivity days
best_prod_day = weekday_avg['Productive Hours'].idxmax()
worst_prod_day = weekday_avg['Productive Hours'].idxmin()

best_nonprod_day = weekday_avg['Worked Hours'].idxmax()
worst_nonprod_day = weekday_avg['Worked Hours'].idxmin()

# Find the month with highest and lowest working hours
best_prod_month = monthly_avg['Productive Hours'].idxmax()
worst_prod_month = monthly_avg['Productive Hours'].idxmin()

best_nonprod_month = monthly_avg['Worked Hours'].idxmax()
worst_nonprod_month = monthly_avg['Worked Hours'].idxmin()

# Display Insights
print("📊 **Overall Averages:**")
print(f" - Avg Total Hours: {avg_tos:.2f} hrs")
print(f" - Avg Productive Hours: {avg_ptos:.2f} hrs")

print("\n📅 **Best & Worst Days for Productivity:**")
print(f" - Most Productive Day: {best_prod_day}")
print(f" - Least Productive Day: {worst_prod_day}")

print("\n⚡ **Best & Worst Days for Totaluctive Hours:**")
print(f" - Highest Working Hours Day: {best_nonprod_day}")
print(f" - Lowest Working Hours Day: {worst_nonprod_day}")

print("\n📆 **Month-wise Productivity Insights:**")
print(f" - Most Productive Month: {best_prod_month}")
print(f" - Least Productive Month: {worst_prod_month}")

print(f" - Highest Total Month: {best_nonprod_month}")
print(f" - Lowest Total Month: {worst_nonprod_month}")

print("\n📈 **Monthly Averages:**")
print(monthly_avg.round(2))

print("\n📅 **Weekday Averages:**")
print(weekday_avg.round(2))
