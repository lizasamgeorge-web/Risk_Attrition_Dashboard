import pandas as pd
import numpy as np

np.random.seed(42)
scale_data= {
    'CustomerID': range(1001,1051),
    'DaysSinceActive': np.random.randint(5,90, size=50),
    'MobileLogins': np.random.randint(0,30, size=50),
    'BalanceDropPercent': np.random.randint(0,100, size=50)
}

df= pd.DataFrame(scale_data)

true_churn= df[(df['DaysSinceActive']>30) & (df['MobileLogins']<5) & (df['BalanceDropPercent']<10)]

print("---ENTERPRISE SEARCH COMPLETE---")
print(f"Total Portfolio Analyzed: {len(df)}Customers")
print(f"High Priority Risks Isolated: {len(true_churn)} Customers\n")
print(true_churn)


df.to_csv('enterprise_churn_data.csv', index=False)

print("\n---- Enterprise Data Exported Successfully ----")
