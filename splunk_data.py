import pandas as pd
data_type = "bytes_from_client" # bytes_from_client bytes_to_server bytes_from_server bytes_to_client
person = "jade"   # 這是用來測試的資料
# 使用 f-string 並正確轉義反斜線
path = f"C:\\Users\\cawang\\Downloads\\{data_type}.csv"
npath = f"C:\\Users\\cawang\\Downloads\\{data_type}_{person}.csv"
# 讀取 CSV 至 pandas DataFrame
df = pd.read_csv(path)
# 刪除 header 值為 null 的欄位
df = df.drop(columns=[col for col in df.columns if pd.isna(col)])
# 保持第0欄不動，其餘欄位按 header 名稱長度排序
first_col = df.columns[0]
other_cols = sorted(df.columns[1:], key=lambda x: len(x))
df = df[[first_col] + other_cols]
# 顯示前幾列
print(df.head())
# 輸出修改後的 DataFrame 到原始檔案位置
df.to_csv(npath, index=False)

client_secret = "oxZ8Q~jrrr2Q1i9XZmJ~6w_ZOC6.OMSpJwTrzrE."
pwd = "efedgrgggergrgergrgr"
