# --------------
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# path- variable storing file path

#Code starts here
df = pd.read_csv(path)
print(df.head())

#Seperating Dependent and Independent Variables
X = df.drop(['Price'], axis=1)
y = df['Price']

#Spiltting Train & Test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=6)

#Finding Correlation
corr = X_train.corr(method ='pearson')
print(corr)




# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Code starts here

#Initiate LinerRegression
regressor = LinearRegression()

#Fit & Predict
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

#Find R2 score
r2 = r2_score(y_test, y_pred)
print(r2)


# --------------
from sklearn.linear_model import Lasso

# Code starts here

#Initiate Lasso Model
lasso = Lasso()

#Create a Lasso Model
lasso.fit(X_train, y_train)
lasso_pred = lasso.predict(X_test)

#Find R2 score for Lasso Model
r2_lasso = r2_score(y_test, lasso_pred)
print(r2_lasso)


# --------------
from sklearn.linear_model import Ridge

# Code starts here

#Initiate Ridge Model
ridge = Ridge()

#Fit & Predict
ridge.fit(X_train, y_train)
ridge_pred = ridge.predict(X_test)

#R2 Score
r2_ridge = r2_score(y_test, ridge_pred)
print(r2_ridge)
# Code ends here


# --------------
from sklearn.model_selection import cross_val_score

#Code starts here

#Initiate Linear Regression
regressor = LinearRegression()

#Calculating cross validation value
score = cross_val_score(regressor, X_train, y_train, cv=10)
mean_score = np.mean(score)

print(mean_score)



# --------------
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

#Code starts here
model = make_pipeline(PolynomialFeatures(2), LinearRegression())

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

r2_poly = r2_score(y_test, y_pred)
print(r2_poly)


