# Question 2: Read data from Excel file using pandas
import pandas

excel_data_df = pandas.read_excel('data1.xlsx', sheet_name='Sheet1')
# print whole sheet data
print("\n Data from Excel file")
print(excel_data_df)

# Question 3: - Calculate the result column = average(Programming, English, Philosophy) and save to new file
# Calculate KQ from 
# Access to column
'''
print("Column programming", excel_data_df['Programming'].tolist())
print("Column english", excel_data_df['English'].tolist())
print("Column philosophy", excel_data_df['Philosophy'].tolist())
'''
# Formula KQ = (LT + Ct + NN)/3 round to 2 digits
# Emnpty LT list
programming = []
programming = excel_data_df['Programming'].tolist()

english = []
english = excel_data_df['English'].tolist()

philosophy = []
philosophy = excel_data_df['Philosophy'].tolist()

ID = []
ID = excel_data_df['ID'].tolist()

name = []
name = excel_data_df['Name'].tolist()

KQ = []
# Calculate KQ
for i in range(0, len(programming)):
    KQ.append(round((programming[i] + english[i] + philosophy[i])/3,2))

#print("KQ = ", KQ)

# Write KQ into  data frame
df = pandas.DataFrame({'ID':ID, 'Name':name , 'KQ': KQ})

df.to_excel('./KQ.xlsx')


# Question 4: Read top 4 lines

# Question 5: Visualization with 4 scores (Programming, English, Philosophy, Result)
import matplotlib.pyplot as plt
plt.plot(programming)
plt.title("Programming scores")
plt.show()

plt.plot(english)
plt.title("English scores")
plt.show()

plt.plot(philosophy)
plt.title("Philosophy scores")
plt.show()

# Question 6: Show Min, Max, Average of 4 scores 
print("\n Describe data from excel file")
print(excel_data_df.describe())

# Question 7: Print out top 5 students with the highest result score
KQ_sheet = pandas.read_excel('KQ.xlsx', sheet_name='Sheet1')
# print whole sheet data
print("\n Data from KQ file")
print(KQ_sheet)

kq_value = []
kq_value = KQ_sheet['KQ'].tolist()
print(kq_value)

from operator import itemgetter
lst = dict(zip(name,kq_value))
top5_lst = dict(sorted(lst.items(), key=itemgetter(1), reverse=True)[:5])

print("\nTop 5 students:")
print(top5_lst)

# Question 8: Calculate Pearson and Spearman (handmade function & Libarary) between Age, Programming, English, Philosophy and Result

# Question 9: 9- Using heatmap to visualize the result of the question 8
