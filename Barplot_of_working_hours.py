import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Excel file
file = r"C:\Users\Vamshi Yempally\Downloads\Date_workinghours.xlsx"
df = pd.read_excel(file)

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%b')  # Abbreviated month (Jan, Feb, ...)
df['Weekday'] = df['Date'].dt.strftime('%a')  # Abbreviated weekday (Mon, Tue, ...)

# Define correct order for sorting
weekday_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create figure with subplots (4 rows, 3 columns)
fig, axes = plt.subplots(4, 3, figsize=(18, 12))
fig.suptitle('Working Hours by Month', fontsize=16)

# Get unique months in proper order
months = sorted(df['Month'].dropna().unique(), key=lambda x: month_order.index(x))

# Define colors for bars
colors = {"TOS": "blue", "PTOS": "orange"}

# Create an empty list to collect bar objects for the legend
handles = []
labels = []

# Loop through each month and create a separate histogram
for i, month in enumerate(months):
    ax = axes[i // 3, i % 3]  # Select subplot location

    # Group data by weekday and calculate the mean TOS & PTOS
    month_data = df[df['Month'] == month].groupby('Weekday')[['TOS', 'PTOS']].mean().reset_index()

    # Sort by correct weekday order
    month_data['Weekday'] = pd.Categorical(month_data['Weekday'], categories=weekday_order, ordered=True)
    month_data = month_data.sort_values('Weekday')

    # Create histogram (bar plot)
    bar1 = sns.barplot(data=month_data, x="Weekday", y="TOS", color=colors["TOS"], label="Tot Hours", ax=ax)
    bar2 = sns.barplot(data=month_data, x="Weekday", y="PTOS", color=colors["PTOS"], label="Prod Hours", ax=ax, alpha=0.7)

    ax.set_title(month)  # Set title for each subplot
    ax.set_xlabel('')
    ax.set_ylabel('')

    # Store only once (first subplot)
    if i == 0:
        handles.extend([bar1.patches[0], bar2.patches[0]])
        labels.extend(["TOS", "PTOS"])

# Create a single legend at the bottom
fig.legend(handles, labels, loc="lower center", ncol=2, fontsize=12)

# Adjust layout for better spacing
plt.subplots_adjust(hspace=0.8, wspace=0.3, bottom=0.1)  # Increase bottom spacing for the legend

plt.show()
