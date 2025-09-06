import pandas as pd

#read all csv files
df1 = pd.read_csv('data/daily_sales_data_0.csv')
df2 = pd.read_csv('data/daily_sales_data_1.csv')
df3 = pd.read_csv('data/daily_sales_data_2.csv')

#combine all csv files into one file
sales_df = pd.concat([df1, df2, df3])

#fix formatting of price and date
sales_df['price'] = sales_df ['price'].str.replace('$', '').astype(float)
sales_df['date'] = pd.to_datetime(sales_df['date'])



#add sales column
sales_df['sales'] = sales_df['price'] * sales_df['quantity']

#filter out only pink morsel
pink_morsel = sales_df[sales_df['product'] == "pink morsel"]

#split up to before 15jan21 and after
before_df = pink_morsel[pink_morsel['date'] < '2021-01-15']
after_df = pink_morsel[pink_morsel['date'] >= '2021-01-15']

#testing
#print(pink_morsel)
#print(before_df)
##print(after_df)

#print("Total sales before 15 jan", len(before_df))
#print("Total sales after 15 jan", len(after_df))
#print("Total sales of pink morsel", len(pink_morsel))

#task 2 final answer
final_db = pink_morsel[['sales', 'date', 'region']]
print(final_db)