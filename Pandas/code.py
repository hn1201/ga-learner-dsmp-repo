# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
# code starts here
bank=pd.read_csv(path,sep=',', delimiter=None)
categorical_var=bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var=bank.select_dtypes(include = 'number')
print(numerical_var)


# code ends here


# --------------
# code starts here
banks=bank.drop(columns=['Loan_ID'])

#print(banks.isnull().sum())
bank_mode=banks.mode()
#print(bank_mode)
banks.fillna('bank_mode', inplace=True)
print(banks)
#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc=np.mean)



# code ends here



# --------------
# code starts here
#print(banks.head(5))
mask_selfemploy=(banks['Self_Employed']=='Yes')
mask_loanstatus=(banks['Loan_Status']=='Y')
mask_selfnemploy=(banks['Self_Employed']=='No')
loan_approved_se=banks[mask_selfemploy][mask_loanstatus].count().iloc[0]
loan_approved_nse=banks[mask_selfnemploy][mask_loanstatus].count().iloc[0]
Loan_Status_count=614
percentage_se=(loan_approved_se/Loan_Status_count)*100
percentage_nse=(loan_approved_nse/Loan_Status_count)*100
print(percentage_se)
print(percentage_nse)
# code ends here


# --------------
# code starts here
loan_term=banks['Loan_Amount_Term'].apply(lambda x : x/12)
big_loan=(loan_term>=25).value_counts()
big_loan_term=554



# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome','Credit_History']
mean_values = loan_groupby.agg([np.mean])
print(mean_values)

# code ends here


