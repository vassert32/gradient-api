from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pickle

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
model = GradientBoostingClassifier()
model.fit(X_train, y_train)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
