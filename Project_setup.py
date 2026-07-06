import os

# ==========================================
# 1. CORE CODE (app.py) AUTOMATION
# ==========================================
app_code = """import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

print("--- Customer Segmentation Project ---")

# Mock customer data (Behavioral & Demographics)
data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Age': [23, 45, 21, 51, 25, 34, 55, 22, 41, 30],
    'Annual_Income_kUSD': [15, 75, 16, 80, 20, 50, 90, 18, 60, 45],
    'Spending_Score': [81, 10, 75, 12, 85, 40, 15, 90, 20, 55]
}
df = pd.DataFrame(data)

# Extract features
X = df[['Annual_Income_kUSD', 'Spending_Score']]

# Scale metrics
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit KMeans model
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster_ID'] = kmeans.fit_predict(X_scaled)

print("\\nProcessing completed. Final target cluster outputs:")
print(df.to_string(index=False))
"""

# ==========================================
# 2. DOCUMENTATION (README.md) AUTOMATION
# ==========================================
readme_text = """# Customer Segmentation Project

## Project Summary
This repository contains a mobile-compatible Machine Learning pipeline built using Python to analyze and group target business customers based on their annual income and spending behaviours.

## Model Setup
- **Framework**: Scikit-Learn
- **Algorithm**: K-Means Clustering
- **Feature Pipeline**: StandardScaler
"""

# ==========================================
# 3. ENVIRONMENT FILE CREATION
# ==========================================
requirements_text = """pandas
scikit-learn
"""

# System writes and saves all project structure automatically
print("Auto-building project directories and files...")

with open("app.py", "w") as f:
    f.write(app_code)
print("-> Successfully structured: app.py")

with open("README.md", "w") as f:
    f.write(readme_text)
print("-> Successfully structured: README.md")

with open("requirements.txt", "w") as f:
    f.write(requirements_text)
print("-> Successfully structured: requirements.txt")

print("\\n[SUCCESS] All project components are organized and ready for deployment!")
