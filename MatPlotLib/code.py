# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path, sep=',', delimiter=None)

#Code starts here
loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind="bar", stacked=True, figsize=(8,8))


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()
#print(property_and_loan)

property_and_loan.plot(kind="bar", stacked=False, figsize=(8,8))
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)


# --------------
#Code starts here

education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()

education_and_loan.plot(kind="bar", stacked=True, figsize=(8,8))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)


# --------------
#Code starts here
graduate=data[data['Education'] == 'Graduate']
#print(graduate)

not_graduate=data[data['Education'] == 'Not Graduate']
#print(not_graduate)

graduate['LoanAmount'].plot(kind="density", label='Graduate')
not_graduate['LoanAmount'].plot(kind="density", label='Not Graduate')








#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(3,1, figsize=(15,10))

ax_1.scatter(data['ApplicantIncome'], data['LoanAmount'])
ax_1.set_title('Applicant Income')

ax_2.scatter(data['CoapplicantIncome'], data['LoanAmount'])
ax_2.set_title('CoapplicantIncome')

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
#print(data['TotalIncome'])

ax_3.scatter(data['TotalIncome'], data['LoanAmount'])
ax_3.set_title('TotalIncome')


