# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
bank = pd.DataFrame(bank_data) 

categorical_var=[bank_data.select_dtypes(include = 'object')]
print(categorical_var)
numerical_var=bank_data.select_dtypes(include = 'number')
print(numerical_var)

banks=bank.drop(['Loan_ID'],axis=1)
banks.isnull().sum()

bank_mode=banks.mode()

banks=banks.fillna(bank_mode)

avg_loan_amount=pd.pivot_table(data=banks,index=('Gender','Married','Self_Employed'),values='LoanAmount',aggfunc='mean')

loan_approved_se=np.logical_and(banks.Self_Employed == 'Yes', banks.Loan_Status == 'Y')
loan_approved_nse=np.logical_and(banks.Self_Employed == 'No' , banks.Loan_Status == 'Y')

percentage_se=loan_approved_se.value_counts(normalize=True).mul(100).astype(str)+'%'
percentage_se
percentage_nse=loan_approved_nse.value_counts(normalize=True).mul(100).astype(str)+'%'
percentage_nse

loan_term=banks.Loan_Amount_Term.apply( lambda x: x/12 )
big_loan_term=loan_term.apply(lambda x : x >=25 ).value_counts().tolist()[0]

loan_groupby=banks.groupby('Loan_Status')['ApplicantIncome', 'Credit_History']
mean_values=loan_groupby.mean()








