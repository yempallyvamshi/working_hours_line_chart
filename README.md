# working_hours_line_chart
# Working Hours Visualization

## Overview
This script reads an Excel file containing working hours data, processes it, and generates a visualization of average TOS and PTOS hours for each weekday in different months using line charts.

## Features
- Reads data from an Excel file.
- Extracts and formats date information into month and weekday.
- Groups data by weekdays within each month.
- Generates multiple subplots (4x3) showing trends in TOS (Non Prod) and PTOS (Prod) working hours.
- Ensures correct ordering of months and weekdays.
- Displays a single figure with well-organized subplots.

## Prerequisites
Ensure you have the following libraries installed before running the script:

```bash
pip install pandas matplotlib seaborn openpyxl
```

## Usage
1. Update the `file` variable with the correct path to your Excel file:
   ```python
   file = r"C:\Users\YourName\Downloads\Date_workinghours.xlsx"
   ```
2. Run the script.
3. The script will generate a figure with subplots displaying working hours trends.

## File Format
The input Excel file should contain at least the following columns:
- `Date`: Date of the working hours entry
- `TOS`: Non-productive working hours
- `PTOS`: Productive working hours

## Output
- A visualization with **12 subplots**, each representing one month.
- **X-axis**: Weekdays (Mon-Sun)
- **Y-axis**: Average working hours.
- Two lines:
  - **Non Prod (TOS)** - Represented with circles.
  - **Prod (PTOS)** - Represented with squares.

## Customizations
- To change line colors or styles, modify the `sns.lineplot()` function parameters.
- To adjust figure layout, tweak `plt.subplots_adjust(hspace, wspace)` values.

## License
This project is open-source. Modify and distribute as needed.
