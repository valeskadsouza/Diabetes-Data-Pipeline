import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import json
from pymongo import MongoClient

# Load data
df = pd.read_csv('../data/processed_batch.csv')

# Features & target
X = df.drop(columns=['readmitted_flag'])
y = df['readmitted_flag']

# Split and train
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(clf, '../data/rf_model.joblib')
print("Model saved to data/rf_model.joblib")

# Store model binary in MongoDB
with open('../config1/mongodb_config1.json') as f:
    cfg = json.load(f)
client = MongoClient(cfg['mongodb_uri'])
db = client[cfg['db_name']]
models = db['trained_models']
with open('../data/rf_model.joblib','rb') as mfile:
    models.insert_one({
        'model_name': 'random_forest_readmission',
        'binary': mfile.read(),
        'metrics': classification_report(y_test, y_pred, output_dict=True)
    })
print("Model stored in MongoDB collection 'trained_models'.")
