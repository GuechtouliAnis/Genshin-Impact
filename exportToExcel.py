import sqlite3
import openpyxl
# Connect to .db file
conn = sqlite3.connect("GI_auto.db")
cursor = conn.cursor()

# Get list of tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
table_list = cursor.fetchall()

# Create an Excel Workbook
wb = openpyxl.Workbook()

# Loop through table list
for table in table_list:
    # Create a sheet
    sheet = wb.create_sheet(table[0])

    # Execute query
    cursor.execute("SELECT * FROM " + table[0])

    # Get column names
    column_names = [description[0] for description in cursor.description]

    # Write column names to the first row of the sheet
    sheet.append(column_names)

    # Fetch results
    results = cursor.fetchall()

    # Populate sheet with results
    for row in results:
        sheet.append(row)

# Save workbook
wb.save("GI_autoExcel.xlsx")