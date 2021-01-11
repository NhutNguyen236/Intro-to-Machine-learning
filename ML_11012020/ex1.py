# Read data from Excel file
import pandas

excel_data_df = pandas.read_excel('data1.xlsx', sheet_name='Sheet1')
print(excel_data_df.describe())

# print whole sheet data
print(excel_data_df)

# Calculate KQ from 
# Access to column

print("Column LT", excel_data_df['LT'].tolist())
print("Column NN", excel_data_df['NN'].tolist())
print("Column CT", excel_data_df['CT'].tolist())

# Formula KQ = (LT + Ct + NN)/3 round to 2 digits
# Emnpty LT list
LT = []
LT = excel_data_df['LT'].tolist()

NN = []
NN = excel_data_df['NN'].tolist()

CT = []
CT = excel_data_df['CT'].tolist()

ID = []
ID = excel_data_df['ID'].tolist()

KQ = []
# Calculate KQ
for i in range(0, len(LT)):
    KQ.append(round((LT[i] + CT[i] + NN[i])/3,2))

print("KQ = ", KQ)

# Write KQ into  data frame
df = pandas.DataFrame({'ID':ID, 'KQ': KQ})

df.to_excel('./KQ.xlsx')

# Plot data
import matplotlib.pyplot

