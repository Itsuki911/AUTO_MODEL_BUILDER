import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def train_model(data):
    X = data['input']
    y = data['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train.values.reshape(-1, 1), y_train)
    predictions = model.predict(X_test.values.reshape(-1, 1))
    accuracy = accuracy_score(y_test, predictions)
    return model, accuracy