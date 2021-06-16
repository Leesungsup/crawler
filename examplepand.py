import pandas as pd
df1=pd.DataFrame({
'이름':['손흥민','음바페','홀란드'],
'나이':[28,22,20],
'소속':['토트넘','PSG','도르트문트']})
print(df1)
list=[
['손흥민',28,'토트넘'],
['음바페',22,'PSG'],
['홀란드',20,'도르트문트']
]
df2=pd.DataFrame(list,columns=['이름','나이','소속'])
print(df2)
