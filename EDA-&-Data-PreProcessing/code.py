# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here
data = pd.read_csv(path)
#print(data.shape)
data.hist(column='Rating')

data = data[data.Rating <= 5]
#print(data.shape)
data.hist(column='Rating')
#(data[data['Rating']<=5]).hist(column='Rating')


#Code ends here


# --------------
# code starts here

total_null = data.isnull().sum()
#print(total_null)
percent_null = (total_null/data.isnull().sum().count())
#print(percent_null)
missing_data = pd.concat((total_null, percent_null), axis=1,  keys=['Total','Percent'])
#print(missing_data)

data.dropna(inplace=True)

total_null_1 = data.isnull().sum()
percent_null_1 = (total_null_1/data.isnull().sum().count())
missing_data_1 = pd.concat((total_null_1, percent_null_1), axis=1,  keys=['Total','Percent'])
print(missing_data_1)
# code ends here


# --------------

#Code starts here
ax = sns.catplot(x='Category', y='Rating', data=data, kind='box', height=10)
ax.set_xticklabels(rotation=90)
plt.title('Rating vs Category [BoxPlot]')
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here

#Removing `,` from the column
data['Installs']=data['Installs'].str.replace(',','')

#Removing `+` from the column
data['Installs']=data['Installs'].str.replace('+','')

#Converting the column to `int` datatype
data['Installs'] = data['Installs'].astype(int)

#Creating a label encoder object
le=LabelEncoder()

#Label encoding the column to reduce the effect of a large range of values
data['Installs']=le.fit_transform(data['Installs'])

#Setting figure size
plt.figure(figsize = (10,10))

#Plotting Regression plot between Rating and Installs
sns.regplot(x="Installs", y="Rating", color = 'teal',data=data)

#Setting the title of the plot
plt.title('Rating vs Installs[RegPlot]',size = 20)

#Code ends here



# --------------
#Code starts here

print(data['Price'].value_counts())

data['Price']=data['Price'].str.replace('$','')
data['Price'] = data['Price'].astype(float)

sns.regplot(x='Price', y='Rating', data=data)
plt.title("Rating vs Price [RegPlot]")
#Code ends here


# --------------

#Code starts here

#print(data['Genres'].unique())

data['Genres'] = data['Genres'].str.split(";").str[0]
#print(data['Genres'].head())

gr_mean = data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()

#gr_mean = data.groupby(['Genres'])[['Rating']].mean().sort_values(by='Rating', ascending=False)
#print(gr_mean.describe())
gr_mean = gr_mean.sort_values(by='Rating')
print(gr_mean.iloc[0])
print(gr_mean.iloc[-1])






#Code ends here


# --------------

#Code starts here
import pandas as pd

#print(data['Last Updated'].head())
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
max_date = data['Last Updated'].max()

data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days
#print(data['Last Updated Days'])

ax = sns.regplot(x='Last Updated Days', y='Rating', data=data)

plt.title('Rating vs Last Updated [RegPlot]')

#Code ends here


