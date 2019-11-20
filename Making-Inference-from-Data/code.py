# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]

#Code starts here
data = pd.read_csv(path, sep=',', delimiter=None)
data_sample = data.sample(n=sample_size, random_state=0)
sample_mean = data_sample['installment'].mean()
sample_std = data_sample['installment'].std()

margin_of_error = z_critical * (sample_std/math.sqrt(sample_size))
#print(margin_of_error)
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
print(confidence_interval)
true_mean = data['installment'].mean()
print(true_mean)



# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
plt.tight_layout()
fig ,axes = plt.subplots(3,1, figsize=(10,10))

for i in range(len(sample_size)) :
    m = [];
    for j in range(1000) :
        dsample = data['installment'].sample(n=sample_size[i], random_state=0)
        m.append(dsample.mean())
    mean_series = pd.Series(m)
    axes[i] = mean_series.hist()



# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
data['int.rate'] = data['int.rate'].str.replace('%',"").astype(float)
data['int.rate'] = data['int.rate'].div(100)
#print(data['int.rate'])
x1 = data[data['purpose']=='small_business']['int.rate']
value = data['int.rate'].mean()
z_statistic, p_value = ztest(data[data['purpose']=='small_business']['int.rate'], value=data['int.rate'].mean(), alternative='larger')
print(z_statistic)
print(p_value)
if p_value < 0.05 : print('Null Hypothesis rejected')
else : print('Null Hypothesis can not be rejected')


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here


z_statistic, p_value = ztest(data[data['paid.back.loan']=='No']['installment'],data[data['paid.back.loan']=='Yes']['installment'], value=0, alternative='two-sided')
z_statistic = round(z_statistic,2)
print(z_statistic)
print(p_value)
if p_value < 0.05 : print('Null Hypothesis rejected')
else : print('Null Hypothesis can not be rejected')


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes = data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
no = data[data['paid.back.loan']=='No']['purpose'].value_counts()
#print(yes)
#print(no)
observed = pd.concat([yes.transpose(), no.transpose()], axis = 1, keys = ['Yes', 'No'])
#print(observed)
chi2, p, dof, ex = chi2_contingency(observed)
print(chi2)
print(critical_value)
if chi2 > critical_value : print('Null Hypo rejected')
else : print('Null Hypo cant be rejected')


