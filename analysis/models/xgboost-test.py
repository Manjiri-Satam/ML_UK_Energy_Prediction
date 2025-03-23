import numpy as np
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import os

git_path = os.path.expanduser('~/git/ml-power/')
data = pd.read_csv(git_path + 'data/df.csv')
results_folder = git_path + 'data/model_results/'

print([f"X[\'kwh\'" + str(i) + f"\']" for i in range(1,29)])

# drop target (kwh), household, and the descriptive columns
X = data.drop(columns=['kwh',
                       'month_abbr', 'acorn_description'])
X['month'] = X['month'].astype('str')
X['year'] = X['year'].astype('str')
X['acorn_category'] = X['acorn_category'].astype('str')
X = pd.get_dummies(X)

X['mean_kwh_last_28_days'] = (X['kwh1'] + \
X['kwh2'] + \
X['kwh3'] + \
X['kwh4'] + \
X['kwh5'] + \
X['kwh6'] + \
X['kwh7'] + \
X['kwh8'] + \
X['kwh9'] + \
X['kwh10'] + \
X['kwh11'] + \
X['kwh12'] + \
X['kwh13'] + \
X['kwh14'] + \
X['kwh15'] + \
X['kwh16'] + \
X['kwh17'] + \
X['kwh18'] + \
X['kwh19'] + \
X['kwh20'] + \
X['kwh21'] + \
X['kwh22'] + \
X['kwh23'] + \
X['kwh24'] + \
X['kwh25'] + \
X['kwh26'] + \
X['kwh27'] ) / 28


y = data['kwh']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

n_estimators = 500
learning_rate = 0.05
max_depth = 5
model = XGBRegressor(objective='reg:squarederror', n_estimators=n_estimators, learning_rate=learning_rate, max_depth=max_depth)
model.fit(X_train, y_train)

y_pred_train = model.predict(X_train)
mse_train = mean_squared_error(y_train, y_pred_train)
print(f'Train Mean Squared Error: {mse_train}')

y_pred_test = model.predict(X_test)
mse_test = mean_squared_error(y_test, y_pred_test)
print(f'Test Mean Squared Error: {mse_test}')

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
}).sort_values(by='Importance', ascending=False)

filename = f'{results_folder}xgboost_nestimators{str(n_estimators)}_learningrate{str(int(learning_rate * 1000))}_maxdepth{str(max_depth)}.txt'
with open(filename, 'w') as file:
    # Write additional text
    file.write('\n' + 'XGBoost' + '\n' + \
               f'Train Mean Squared Error: {mse_train}' + '\n' + \
               f'Test Mean Squared Error: {mse_test}' + '\n' + 
               'Feature Importance')
    file.write(feature_importance.to_string(index=False))
