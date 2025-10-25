import pandas as pd

df = pd.read_excel("任意のエクセル.xlsx")

df = df.replace('△', '-', regex=True)
df = df.fillna('')

df.to_excel("cleaned_data.xlsx", index=False)

print("クリーニングが完了しました！")