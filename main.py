import pandas as pd

data_file = "data/2025_booth_signup_unit.csv"
# Read the CSV (adjust the file name and delimiter as needed)
df = pd.read_csv(data_file, header=None)

# Check how many columns we have
print("Number of columns in DataFrame:", len(df.columns))  # Should print 26

# Define the column names list with 26 names
df.columns = [
    "Name", "Address", "Address2", "Door", "City", "State", "Zip", "Blank1", 
    "Phone", "Email", "Blank2", "Blank3", "EventDate", "StartTime", "EndTime", 
    "Duration", "Avail_Slots", "TroopID", "X", "TroopContact", "T1", "T2", "T3", 
    "T4", "BoothSignups", "Extra"
]

# Proceed with converting the BoothSignups column to numeric, etc.
df["BoothSignups"] = pd.to_numeric(df["BoothSignups"], errors="coerce").fillna(0)

# Now group by TroopID and aggregate the signup information
agg = df.groupby("TroopID")["BoothSignups"].agg(
    Total_Booth_Signups="sum",
    Number_of_Booths="count",
    Average_Booth_Signups="mean",
    Min_Booth_Signups="min",
    Max_Booth_Signups="max"
).reset_index()

# Round the average if desired
agg["Average_Booth_Signups"] = agg["Average_Booth_Signups"].round(1)

# Save the summary to a new CSV file
agg.to_csv("booth_signups_per_troop_summary.csv", index=False)
