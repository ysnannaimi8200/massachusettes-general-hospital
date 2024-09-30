import pandas as pd 
import texto_cleaner as t



# this function is for reading the CSV and exel file 
def read_my_files(file_path):
     if file_path.endswith('.csv'):
         c = pd.read_csv(file_path,delimiter = ':')
         t.teg_korchi(c)
         return c
    
     elif file_path.endswith('.xlsx'):
          c = pd.read_excel(file_path)
          t.teg_korchi(c)
          return c
     else:
        print('no csv or xlsx here we procced to json')
        pass
#---------------------------------------------------------------------------------------------------------------#

# function main load the data on my function for the test 
def main(data):
    data1 = read_my_files(file_path)
    # that original # data1 = read_my_files(file_path)

#---------------------------------------------------------------------------------------------------------------#
    
# Testing the functions
if __name__ == "__main__":
    
    #file_path = 'C:/Users/yassi/Desktop/jobintech/data analytics app/Data Analytics Project/Dataset/updated_encounters.xlsx'
    #file_path = 'C:/Users/yassi/Desktop/jobintech/data analytics app/Data Analytics Project/Dataset/patients.csv'  # Use an actual CSV file path to test read_my_files
    file_path = 'C:/Users/yassi/Desktop/jobintech/data analytics app/Data Analytics Project/Dataset/patients.csv'  # Use an actual CSV file path to test read_my_files

    main(file_path)
