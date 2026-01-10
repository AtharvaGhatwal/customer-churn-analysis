import pandas as pd

# load data
df = pd.read_csv("data/bank_churn.csv")

# basic checks
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)

# churn distribution
print("\nChurn distribution:")
print(df["churn"].value_counts())

print("\nChurn percentage:")
print(df["churn"].value_counts(normalize=True) * 100)

# drop useless columns
df = df.drop(columns=["customer_id"])

print("\nColumns after dropping customer_id:")
print(df.columns)

# encode gender (binary)
df["gender"] = df["gender"].map({"Male": 1, "Female": 0})

# one-hot encode country
df = pd.get_dummies(df, columns=["country"], drop_first=True)

print("\nColumns after encoding:")
print(df.columns)

print("\nSample rows after encoding:")
print(df.head())

# split features and target
X = df.drop(columns=["churn"])
y = df["churn"]

print("\nFeature matrix shape (X):", X.shape)
print("Target vector shape (y):", y.shape)

print("\nFeature columns:")
print(X.columns)

from sklearn.model_selection import train_test_split

# train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTrain/Test shapes:")
print("X_train:", X_train.shape)
print("X_test :", X_test.shape)
print("y_train:", y_train.shape)
print("y_test :", y_test.shape)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# initialize logistic regression
model = LogisticRegression(max_iter=1000, class_weight="balanced")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nLOGISTIC REGRESSION RESULTS")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

from sklearn.ensemble import RandomForestClassifier

# initialize random forest
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

print("\nRANDOM FOREST RESULTS")
print(confusion_matrix(y_test, rf_pred))
print(classification_report(y_test, rf_pred))

# feature importance
feature_importance = pd.DataFrame({
    "feature": X.columns,
    "importance": rf_model.feature_importances_
}).sort_values(by="importance", ascending=False)

print("\nTOP FEATURES DRIVING CHURN:")
print(feature_importance.head(10))

# ===== EXPORT DATA FOR POWER BI =====

powerbi_df = X_test.copy()
powerbi_df["actual_churn"] = y_test.values
powerbi_df["predicted_churn"] = rf_pred

powerbi_df.to_csv("data/powerbi_churn_data.csv", index=False)

print("\nPower BI dataset exported as data/powerbi_churn_data.csv")
