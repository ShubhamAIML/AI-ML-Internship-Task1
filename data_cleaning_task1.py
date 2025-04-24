import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Import and explore the dataset
df = pd.read_csv('Titanic-Dataset.csv')
print("Dataset Info:")
print(df.info())
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Step 2: Handle missing values
# Fill missing 'Age' with median, ensuring no negative values
df['Age'] = df['Age'].fillna(df['Age'].median()).clip(lower=0)
# Fill missing 'Embarked' with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
# Drop 'Cabin' due to high number of missing values
df.drop(columns=['Cabin'], inplace=True)

# Step 3: Visualize data with boxplots for 'Age' and 'Fare'
plt.figure(figsize=(10, 5))
sns.boxplot(data=df[['Age', 'Fare']])
plt.title('Boxplot of Age and Fare')
plt.savefig('boxplot_age_fare.png')
plt.show()

# Step 4: Verify missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Step 5: Save the cleaned dataset
df.to_csv('cleaned_titanic_with_graphs.csv', index=False)
print("Cleaned dataset saved as 'cleaned_titanic_with_graphs.csv'")
