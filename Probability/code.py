# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path, sep=',', delimiter=None)
p_a = len(df[df['fico']>700])/len(df)
print(p_a)
p_b = len(df[df['purpose']=='debt_consolidation'])/len(df)
print(p_b)
df1 = df[df['purpose']=='debt_consolidation']
df2 = df[df['fico']>700]
#p_a_b = len(df2[df2['purpose']=='debt_consolidation'])/len(df2)
p_a_b = df1[df1['fico'].astype(float) >700].shape[0]/df1.shape[0]
print(p_a_b)
result = (p_a == p_a_b)
print(result)
# code ends here


# --------------
# code starts here
prob_lp = df[df['paid.back.loan'].astype(str) =='Yes'].shape[0]/df.shape[0]
print(prob_lp)
prob_cs = df[df['credit.policy'].astype(str) =='Yes'].shape[0]/df.shape[0]
print(prob_cs)
new_df = df[df['paid.back.loan'].astype(str) =='Yes']
prob_pd_cs = new_df[new_df['credit.policy'].astype(str) =='Yes'].shape[0]/new_df.shape[0]
print(prob_pd_cs)
bayes = (prob_pd_cs*prob_lp)/prob_cs
print(bayes)
# code ends here


# --------------
# code starts here
df['purpose'].value_counts().plot(kind="bar", figsize=(5,5))
plt.xlabel('Loan Reason')
plt.ylabel('No. of Loans')
df1 = df[df['paid.back.loan']=='No']
df1['purpose'].value_counts().plot(kind="bar", figsize=(5,5))
# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
print(inst_median)
inst_mean = df['installment'].mean()
print(inst_mean)
df.hist(column='installment', bins=8, figsize=(5,5))
df.hist(column='log.annual.inc', bins=8, figsize=(5,5))
# code ends here


