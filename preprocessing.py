import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Users\Lenovo\churn_prediction\data\Teleco-Customer-churn.csv"
)

print('orignal dataset shape',df.shape)

# handle missing values
df['TotalCharges']=pd.to_numeric(df['TotalCharges'],errors='coerce')

# drop rows with missing values
df.dropna(inplace=True)
print('after dropping missing values',df.shape)

# duplicates
duplicates=df.duplicated().sum()
print('No of duplicate rows:',duplicates)

if duplicates>0:
    df.drop_duplicates()
    print('After removing duplicates',df.shape)

if 'customerID' in df.columns:
    df.drop('customerID',axis=1,inplace=True)

#-----
numeric_cols=['tenure', 'MonthlyCharges', 'TotalCharges']
for col in numeric_cols:
    plt.figure(figsize=(6,4))
    sns.boxplot(x='Churn',y=col,data=df)
    plt.title(f'{col} vs churn')
    plt.show()
    plt.savefig("churn_distribution.png")
    plt.close()
           


df['Churn']=df['Churn'].map({'Yes':1,'No':0})


# Encode categorical features
categorical_cols=df.select_dtypes(include=['object']).columns
df=pd.get_dummies(df,columns=categorical_cols,drop_first=True)

# split into featues and target
X=df.drop('Churn',axis=1)
y=df['Churn']

# train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

print('Train Shape:',X_train.shape)
print('Test Shape:',X_test.shape)



X_train.to_csv('data/X_train.csv',index=False)
X_test.to_csv('data/X_test.csv',index=False)
y_train.to_csv('data/y_train.csv',index=False)
y_test.to_csv('data/y_test.csv', index=False)








