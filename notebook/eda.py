import pandas as pd

df=pd.read_csv("data/Teleco-Customer-churn.csv")

print(df.head())

print('datset info')
print(df.info(),'\n')

#check missing values

print('missing values in each column')

print(df.isnull().sum(),'\n')

if 'Churn' in df.columns:
    print("\n===== Target Variable Distribution (Churn) =====")
    print(df['Churn'].value_counts())
else:
    print("\nChurn column not found!")


categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

print('\n unique values in categorical columns')
for col in categorical_cols:
    print(f'{col}:{df[col].unique()}')

