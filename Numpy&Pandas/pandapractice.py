import numpy as np
import pandas as pd
import os

'''Pandas Series and Numpy Array'''

# price_list = [100, 200, 300, 400, 500]
# med_price_array  =  np.array(price_list)
# series_list = pd.Series(price_list)
# series_list2 = pd.Series(med_price_array)   
# print(series_list)
# print(series_list2)


# price_list_labeled = pd.Series(price_list, index=['Omeprazole', 'Azethromycine', 'MMeta', 'profim', 'Paracetamol'])
# print(price_list_labeled)

# price_list_labeled = price_list_labeled + 2
# print(price_list_labeled)

# new_price_list = pd.Series([100, 200, 300, 400, 500], index=['Omeprazole', 'Azethromycine', 'MMeta', 'profim', 'Paracetamol'])
# print(new_price_list - price_list_labeled)


'''Pandas DataFrame and Numpy Array'''

# student = ['John', 'Jane', 'Tom', 'Jerry']
# student_data_frame = pd.DataFrame(student, columns=['Student'])
# print(student_data_frame)

# grades= [90, 80, 85, 95]
# # Creating a DataFrame with two columns: Student and Grade
# print(pd.DataFrame({'Student' : student, 'Grade' : grades}))

# series1 = pd.Series([1, 2, 3])
# series2 = pd.Series([4, 5, 6])
# print(pd.DataFrame({'A': series1, 'B': series2}))

# print(pd.DataFrame(np.random.randn(5,2), columns=['Trial 1', 'Trial 2'])) # 5 rows and 2 columns of random numbers

'''Pandas Accessing series'''

# operators = ['AT&T', 'Verizon', 'T-Mobile']
# revenue = [100, 200, 300]
# telecom = pd.Series(revenue, index=operators)
# print(telecom, telecom[0])
# print(telecom[1:3]) # slicing
# print(telecom[telecom > 100]) # boolean indexing
# print(telecom[['AT&T', 'T-Mobile']]) # indexing with labels

'''Pandas Accessing DataFrame'''

store_data = pd.DataFrame({'CustomerId' : [1, 2, 3, 4], 
                           'Name' : ['John', 'Jane', 'Tom', 'Jerry'],
                           'Age' : [25, 30, 35, 40],
                           'City' : ['New York', 'Los Angeles', 'Chicago', 'Houston']})

# print(store_data)

'''loc and iloc'''

# print(store_data['Name']) # Accessing a single column / dimension
# print(store_data[['Name', 'Age']]) # Accessing multiple columns / dimenstions 
# print(store_data[:3]) # Accessing a range of rows
# print(store_data[store_data['Age'] > 30]) # Accessing rows based on a condition
# print(store_data[::2]) # Accessing every other row
# print(store_data[store_data['Name'].isin(['John', 'Tom'])]) # Accessing rows based on a list of values


# print(store_data.loc[1]) # Accessing a row by label
# print(store_data.loc[[1,3],['Name','Age']]) # Accessing a row by index
# print(store_data.loc[store_data['Age'] > 30, ['Name', 'City']]) # Accessing a row by condition

# print(stored_data.iloc[1]) # Accessing a row by index
# print(store_data.iloc[[1,3], [1,2]]) # Accessing a row by index
# print(store_data.iloc[store_data['Age'] > 30, [1,3]]) # Accessing a row by condition    

# store_data.loc[3, 'Age'] = 45 # Updating a value in the DataFrame
# print(store_data)    

store_data['rating'] = [4.5, 3.8, 4.2, 4.0] # Adding a new column to the DataFrame
# print(store_data)
# store_data['rating'] = store_data['rating'] + 1 # Updating a column in the DataFrame  

# store_data.drop('rating', axis=1, inplace=True) # Dropping a column from the DataFrame;
#if inplace is not used, it will not be dropped from the original DataFrame and create a new DataFrame
# print(store_data)

# new_storedata = store_data.copy() # Dropping rows from the DataFrame
# print(new_storedata)
# new_storedata.drop([0, 1], inplace=True) # Dropping rows from the DataFrame
# print(new_storedata)
# print(store_data)
# print(store_data.reset_index(drop=True)) # Resetting the index of the DataFrame
# print(store_data.set_index('Name')) # Setting a column as the index of the DataFrame  


store_data_new = pd.DataFrame({'CustomerId' : [2, 3, 4,5,6], 
                           'Sales' : [ 200, 300, 400,500,600],
                           'Distance' : [30, 35, 40,50,60],
                           'City' : ['Los Angeles', 'Chicago', 'Houston', 'bombay', 'delhi']})

# print(pd.concat([store_data, store_data_new], axis=0))
# print(pd.concat([store_data, store_data_new], axis=1))

# inner_join = pd.merge(store_data, store_data_new, on='CustomerId', how='inner') # Merging two DataFrames = Intersection of two DataFrames
# outer_join = pd.merge(store_data, store_data_new, on='CustomerId', how='outer') # Merging two DataFrames = union of two DataFrames 
# print(inner_join)
# print(outer_join)


# print(pd.merge(store_data, store_data_new, on='CustomerId', how='right')) # Merging two DataFrames = right join of two DataFrames
# print(pd.merge(store_data, store_data_new, on='CustomerId', how='left')) # Merging two DataFrames = left join of two DataFrames



'''load folder and read csv file'''
# i need to read stockdata.csv file from the folder Datasets
# i need to read the file into a pandas dataframe
# i need to print the first 5 rows of the dataframe 


print("Current Working Directory:", os.getcwd())

csv_file_path = 'Numpy&Pandas/Datasets/StockData.csv'
excel_file_path = 'Numpy&Pandas/Datasets/StockData.xlsx'

#check if the excel file exists
if os.path.exists(excel_file_path):
    data_frame = pd.read_excel(excel_file_path)
    print(data_frame.head())
else:
    print(f"File not found: {csv_file_path}")

if os.path.exists(csv_file_path):
    data_frame = pd.read_csv(csv_file_path)
    print(data_frame.head()) # Display the first 5 rows of the DataFrame
    
else:
    print(f"File not found: {csv_file_path}")
    
# save the dataframe to a new csv file
data_frame.to_csv('Numpy&Pandas/Datasets/StockData_new.csv', index=False) # Save the DataFrame to a new CSV file
# save the dataframe to a new excel file
data_frame.to_excel('Numpy&Pandas/Datasets/StockData_new.xlsx', index=False) # Save the DataFrame to a new Excel file