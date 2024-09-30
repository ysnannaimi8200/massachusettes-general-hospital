import pandas as pd
import numpy as np

def teg_korchi(c):
    #checking my columns types here 
    print(c.dtypes)
    print ('--------------------------------------------------------------------------')
    #checking the missing value
    print(c.isnull().sum())
    print ('--------------------------------------------------------------------------')
    c = c.apply(lambda x: x.fillna(111111111) if x.dtype == 'float64' else x.fillna('other'))
    print(c)
    print ('--------------------------------------------------------------------------')

    print(c.dtypes)
    print ('--------------------------------------------------------------------------')

    
    pass
    print('here we go , no missing values anymore go ahead')
    # Remove duplicate rows
    if c.duplicated().any():
        print('kayna aweld 3emi kayna ')
        #x = c.duplicated()
        duplicated = c[c.duplicated(keep=False)]
        duplicated.to_excel('C:/Users/yassi/Desktop/jobintech/data analytics app/Data Analytics Project/Dataset/cleaned_dataset_V1/patients________dupli_omira_tegegh_id.xlsx', index=False)
        c = c.drop_duplicates()
        print(c.sum(),'here is the dropped duplicates')
        print ('--------------------------------------------------------------------------')
    else:
        
        print ('--------------------------------------------------------------------------')
        print ('you good there is no dupli go farther with your cleaning ')
        print ('--------------------------------------------------------------------------')
    pass
    # Clean column names (upper case and replace spaces with underscores)
    c.columns = [col.strip().upper() for col in c.columns]
    
    # Convert all string values to uppercase
    #c = c.applymap(lambda x: x.upper() if isinstance(x, str) else x)
    #c = c.apply(lambda x: x.str.upper() if isinstance(x, str) else x)
    # i used this line because it matches with all the types i think 
    c = c.apply(lambda x: x.str.upper() if x.dtype == 'object' else x)
    #c['BIRTHDATE'] = pd.to_datetime(c['BIRTHDATE'].str.replace('|', '-').str.rstrip('Z'), format='%Y-%m-%dT%H:%M:%S').dt.strftime('%m/%d/%Y %I:%M:%S %p')
    print('date a9et mlih')

    
    # Save to Excel file
    #c.to_excel('C:/Users/yassi/Desktop/jobintech/data analytics app/Data Analytics Project/Dataset/updated_payers__V(yzaan).xlsx', index=False)
    c.to_csv('C:/Users/yassi/Desktop/jobintech/data analytics app/Data Analytics Project/Dataset/patient_with_ID.csv', index=False)
    print("Yeeaaah boi")
    # Use an actual CSV file path to test read_my_files'
    
    ###  open refine query transform ###
    ## value.replace("|", "-").toDate().toString("dd-MM-yyyy") ##