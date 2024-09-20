import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report

# Simulate larger data for illustration
np.random.seed(42)
num_samples = 100  # Increase the number of samples
peptides = [''.join(np.random.choice(list('ACDEFGHIKLMNPQRSTVWY'), 9)) for _ in range(num_samples)]
bindings = np.random.choice([0, 1], size=num_samples)  # Random binary labels

# Create DataFrame
df = pd.DataFrame({
    'peptide': peptides,
    'binding': bindings
})

# Define the amino acids
amino_acids = 'ACDEFGHIKLMNPQRSTVWY'

# Function to one-hot encode a peptide sequence
def one_hot_encode(peptide, max_len=9):
    encoding = np.zeros((max_len, len(amino_acids)))
    for i, aa in enumerate(peptide):
        if i < max_len and aa in amino_acids:
            encoding[i, amino_acids.index(aa)] = 1
    return encoding.flatten()

# Apply one-hot encoding to all peptides
df['features'] = df['peptide'].apply(one_hot_encode)

# Split data into features (X) and labels (y)
X = np.stack(df['features'].values)
y = df['binding']

# Stratified split to maintain class proportions
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

# Create and tune the Random Forest model
model = RandomForestClassifier(random_state=42)
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}
grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Best model
best_model = grid_search.best_estimator_

# Make predictions
y_pred = best_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))
