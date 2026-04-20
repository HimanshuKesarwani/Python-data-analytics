import os
import datetime as dt
import csv


def csv_to_dict_of_lists(filepath):
    data = {}
    with open(filepath, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Get the header row

        # Initialize dictionary with empty lists for each header
        for col_name in header:
            data[col_name] = []

        # Populate the dictionary with data
        for row in reader:
            for i, value in enumerate(row):
                data[header[i]].append(value)
    return data

folder_str = [
    'NamasteKart/incoming_files',
    'NamasteKart/success_files',
    'NamasteKart/rejected_files'
]

#os.chdir(f"{os.getcwd()}\\Project_namastekart")
# Create the folders
#for path in folder_str:
#    os.makedirs(path, exist_ok=True) # exist_ok=True prevents an error if the directory already exists
print(os.getcwd())
product_master = csv_to_dict_of_lists('product_master.csv')
print(product_master)
for file in folder_str:
    os.chdir(f"{os.getcwd()}/{folder_str[0]}/{dt.datetime.today().strftime('%Y%m%d')}")
    for csv in os.listdir():
        order_table = csv_to_dict_of_lists(csv)
        # 1- product id should be present in product master table
        if set(order_table['product_id']).issubset(product_master['product_id']):
            print("product id present in master table")
        else:
            print("product id not in master table")

        #2- total sales amount should be (product price from product master table * quantity)
        for element in order_table['product_id']:
            if element in product_master['product_id']:
                if

print(os.getcwd())

#print(dt.datetime.today().strftime('%Y%m%d'))

#Code for getting files in the incoming_files folder
#os.chdir("NamasteKart/incoming_files")
#os.mkdir(f"NamasteKart/incoming_files/{dt.datetime.today().strftime('%Y%m%d')}")

#Code for reading from files of current day
#for path in (f"NamasteKart/incoming_files/{dt.datetime.today().strftime('%Y%m%d')}" ):
print(os.getcwd())
os.chdir(f"{os.getcwd()}/{folder_str[0]}/{dt.datetime.today().strftime('%Y%m%d')}")
file_list=os.listdir()
for file in  file_list:
    #if file[0]=='orders_1.csv' :
    with open(file,'r') as f:
        order_table = f.read()
        print(order_table.split(","or"\n"))


#os.chdir(f"../../..")
print(os.getcwd())

#print(os.listdir())

#for path in

