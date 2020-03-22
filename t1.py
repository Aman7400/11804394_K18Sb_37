from pathlib import Path
import pandas as pd
df = pd.read_excel (Path('C:/Users/Divyanshu/Documents/Train.xlsx'))    
print (df)
n=int(input())
for i in range df:
    if(df[i]==n):
        print(df[i])

