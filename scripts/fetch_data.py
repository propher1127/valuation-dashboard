import akshare as ak
import json
import os  # <--- 必须有这个

# ...（中间获取数据的代码）

# 写入JSON文件（确保文件夹存在）
os.makedirs("data", exist_ok=True)  # <--- 必须有这个
with open("data/valuation.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
