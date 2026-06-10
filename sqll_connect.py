import pandas as pd
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="123456789@",
    database="churn"
)

query = "SELECT * FROM Social_Network_Ads"

df = pd.read_sql(query, conn)

print(df.head())
print(df.shape)



df = df.drop(columns=['User ID', 'Gender'])
x = df.drop(columns=['Purchased'])
y = df['Purchased']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(x_train, y_train)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)

import joblib

joblib.dump(rf, 'rf_model.pkl')
print("Model trained and saved as rf_model.pkl")