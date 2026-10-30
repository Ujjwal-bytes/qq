import matplotlib.pyplot as plt 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
from sklearn.neural_network import MLPClassifier 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report 
iris = load_iris() 
X = iris.data 
 
y = iris.target 
X_train, X_test, y_train, y_test = train_test_split( 
    X, y, test_size=0.3, random_state=42 
)  
scaler = StandardScaler() 
X_train = scaler.fit_transform(X_train) 
X_test = scaler.transform(X_test) 
 
model = MLPClassifier( 
    hidden_layer_sizes=(5,), 
    max_iter=500, 
    random_state=42 
) 
 
model.fit(X_train, y_train)  
y_pred = model.predict(X_test) 
accuracy = accuracy_score(y_test, y_pred) 
 
print("Accuracy:", accuracy) 
 
print("\nConfusion Matrix:") 
print(confusion_matrix(y_test, y_pred)) 
 
print("\nClassification Report:") 
print(classification_report(y_test, y_pred))  
plt.figure(figsize=(8,5)) 
plt.plot(model.loss_curve_) 
plt.title("Training Loss Curve") 
 
plt.xlabel("Iterations") 
plt.ylabel("Loss") 
plt.grid(True) 
plt.show()
