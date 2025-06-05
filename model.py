import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
df = pd.read_excel("Dataset.xlsx")  # Make sure this file is in the same folder

# Clean data
df = df.dropna(subset=["Aggregate rating"])
df.fillna("Unknown", inplace=True)

# Label Encoding
le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col].astype(str))

# Split features and target
X = df.drop("Aggregate rating", axis=1)
y = df["Aggregate rating"]

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "model.pkl")
