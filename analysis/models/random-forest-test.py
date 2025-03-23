import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


data = pd.read_csv('~/git/ml-power/data/df.csv')

# drop target (kwh), household, and the descriptive columns
X = data.drop(columns=['kwh',
                       'month_abbr', 'acorn_description'])
X = pd.get_dummies(X)

features = X.columns.tolist()[1:]

# experimental
# alternative is to convert to 
y = data['kwh']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(n_estimators=100, random_state=1997)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

feature_importances = model.feature_importances_

for ii, feature_importance in enumerate(feature_importances):
    print(f'{features[ii]}: {feature_importance}')