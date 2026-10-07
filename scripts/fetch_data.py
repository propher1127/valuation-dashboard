import akshare as ak
import json
from datetime import datetime

# 需要获取的指数列表
indices = {
    "上证指数": "000001",
    "创业板指": "399006",
    "沪深300": "000300",
    "中证500": "000905",
    "中证1000": "000852"
}

result = {}

for name, code in indices.items():
    try:
        # 使用AkShare获取指数估值数据
        # 注意：不同指数可能需要不同的接口，以下为示例
        df = ak.index_value_hist_funddb(symbol=name)
        latest = df.iloc[-1]
        result[name] = {
            "pe": float(latest["市盈率"]),
            "date": str(latest["日期"])
        }
        print(f"成功获取 {name}: PE={result[name]['pe']}")
    except Exception as e:
        print(f"获取 {name} 失败: {e}")
        result[name] = {"pe": None, "date": None}

# 写入JSON文件
with open("data/valuation.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("数据抓取完成")