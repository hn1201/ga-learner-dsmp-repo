# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path, sep=',', delimiter=None)
data['Gender'].replace(to_replace="-", value="Agender", inplace=True)
#print(data)
gender_count = data['Gender'].value_counts()
gender_count.plot(kind='bar', stacked=False, figsize=(5,5))
plt.ylabel("No. of SHeros")
plt.xticks(rotation=45)

#Code starts here 




# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
print(alignment)
alignment.plot(kind='pie', label="Character Alignment" ,autopct="%1.1f%%")



# --------------
#Code starts here
sc_df = data[['Strength', 'Combat']]
ic_df = data[['Intelligence', 'Combat']]

sc_covariance = sc_df.Strength.cov(sc_df.Combat)
ic_covariance = ic_df.Intelligence.cov(ic_df.Combat)

sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()

ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()

sc_pearson = sc_covariance / (sc_strength * sc_combat)
print(sc_pearson)

ic_pearson = ic_covariance / (ic_intelligence * ic_combat)
print(ic_pearson)



# --------------
#Code starts here
total_high = data['Total'].quantile(q=0.99)

super_best = data[data['Total'] > total_high]

super_best_names = list(super_best['Name'])
print(super_best_names)
print(type(super_best_names))


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(1,3)
ax_1.boxplot(super_best['Intelligence'])
ax_2.boxplot(super_best['Speed'])
ax_3.boxplot(super_best['Power'])
ax_1.set_title('Intelligence')
ax_2.set_title('Speed')
ax_3.set_title('Power')
#fig.subplots_adjust(hspace=0.7)
plt.tight_layout()


