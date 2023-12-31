import pandas as pd
import random

lastnames = ["王", "李", "张", "刘", "陈", "杨", "黄", "吴", "赵", "孙",
    "周", "马", "朱", "胡", "郭", "林", "徐", "李", "梁", "宋",
    "郑", "唐", "冯", "于", "董", "萧", "程", "曹", "袁", "邓",
    "许", "傅", "沈", "曾", "彭", "吕", "苏", "卢", "蒋", "蔡",
    "贾", "丁", "魏", "薛", "叶", "阎", "余", "潘", "杜", "戴",
    "夏", "钟", "汪", "田", "任", "姜", "范", "方", "石", "姚",
    "谢", "程", "邹", "熊", "金", "余", "夏", "毛", "俞", "万",
    "段", "郝", "邱", "卫", "蒋", "祝", "付", "曹", "黎", "马",
    "汤", "滕", "白", "怀", "蒋", "卓", "单"]
firstnames = [ "明", "丽", "伟", "芳", "勇", "秀", "强", "敏", "军", "娟",
    "杰", "婷", "涛", "娜", "鹏", "玲", "刚", "丹", "超", "红",
    "浩", "燕", "鑫", "霞", "健", "萍", "杰", "娣", "洋", "慧",
    "宇", "秋", "鹰", "云", "鑫", "莉", "雷", "莹", "飞", "琴",
    "文", "欣", "兵", "琳", "骏", "美", "峰", "玉", "毅", "丽",
    "冰", "创", "玉", "阳", "宏", "蓉", "建", "欢", "宁", "波",
    "琴", "平", "宝", "东", "晶", "刚", "娥", "恒", "怡", "伦",
    "芬", "宝", "华", "艳", "磊", "佳", "明", "琪", "东", "蓓",
    "弘", "倩", "冬", "良", "帆", "蕾", "生", "巍", "阳", "婷",
    "林", "颖", "齐", "倩", "正", "骏", "楠", "泉", "卫", "婷",
    "宇", "紫", "枫", "金", "静", "振", "鸣", "花", "志", "媛"]

random_names = [random.choice(lastnames) + random.choice(firstnames) + random.choice(firstnames) for _ in range(50)]
df = pd.DataFrame(random_names, columns=["姓名"])
gang = df[df["姓名"].str.contains("刚")].shape[0]

print(gang)