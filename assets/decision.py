import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
from sklearn import tree

# Load the dataset
data = pd.read_csv('dishes_sales.csv')

# Features and target
X = data[['Price (Rs.)', 'Orders (Sales)', 'Rating (out of 5)']]  # Features
y = data['Is Best Dish (Target)']  # Target

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Decision Tree classifier
clf = DecisionTreeClassifier(random_state=42, max_depth=3)  # Limit depth to avoid overfitting
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Visualize the Decision Tree
plt.figure(figsize=(12, 8))
tree.plot_tree(clf, feature_names=X.columns, class_names=['No', 'Yes'], filled=True, rounded=True)
plt.title("Decision Tree for Classifying Best Dishes")
plt.show()

# Example prediction for a new dish
new_dish = pd.DataFrame({
    'Price (Rs.)': [400],
    'Orders (Sales)': [180],
    'Rating (out of 5)': [4.7]
})
prediction = clf.predict(new_dish)
print(f"\nPrediction for new dish: {prediction[0]}")