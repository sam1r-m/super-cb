# Using pandas for data transformations and io to read string as a file
import pandas as pd
import io

data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'
df = pd.read_csv(io.StringIO(data), sep=';')

print(df)
#print(df[FlightCodes].dtypes)

# Convert datatype
df['FlightCodes'] = pd.to_numeric(df['FlightCodes'])

# Fill in missing FlightCodes
start = df['FlightCodes'].dropna().iloc[0] # First non-null row
codes = []

for i in range(len(df)):
    codes.append(int(start + (i * 10))) # Increase by 10 for each row

df['FlightCodes'] = codes

# Split To // From columns and convert to capital case
df[['To', 'From']] = df['To_From'].str.split('_', expand=True)
df['To'] = df['To'].str.title()
df['From'] = df['From'].str.title()

# Remove all punctuation/special characters
df['Airline Code'] = df['Airline Code'].str.replace(r'[^A-Za-z ]', '', regex=True).str.strip()

df = df[['Airline Code', 'DelayTimes', 'FlightCodes', 'From', 'To']]

print(df['FlightCodes'].dtypes)
print(df)
