from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def train_model():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    return model, accuracy
