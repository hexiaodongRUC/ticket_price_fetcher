# data_processing.py

import pandas as pd
import datetime

def remove_chars(s, chars):
    for char in chars:
        s = s.replace(char, '')
    return s

def process_data(ticket_prices_dict):
    # 将从网页获取的内容清洗加工到pandas数组中，便于后面存储，统计，计算
    arr = []
    for idx in ticket_prices_dict.keys():
        for row in ticket_prices_dict[idx]:
            arr.append([idx] + row)
    columns = ["起始地-目的地", "航空公司", "价格", "飞行方式", "总时长", "出发时间", "到达时间"]
    df = pd.DataFrame(arr, columns=columns, index=None)
    df['价格'] = df['价格'].apply(lambda x:int(remove_chars(x[3:], ",")))
    df["数据日期"] = datetime.date.today()
    return df

def save_to_csv(df, filename):
    df.to_csv(filename, mode="a", index=False, header=False)