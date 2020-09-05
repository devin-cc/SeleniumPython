"""
    目标：将python中的字典转换程json字符串
    案例：data = {"name":"张三", "age":"18"}
    操作：
        json中：还有一个方法dump()写入json，勿要选错
"""

# 导包
import json

"""将字典转换成json字符串"""
# 定义 字典
# data1 = {"name": "张三", "age": "18"}

# # 调用dumps转化为json
# print("转换之前的数据类型：", type(data1))
# d2 = json.dumps(data1)
# print("转换之后的数据类型", type(d2))
# print(d2)


"""
    目标：将字符串转换成json
    方法：loads()将字符串转为字典
    注意：load() 此方法为读取json方法，千万别写错
"""

# data2 = '{"name": "张三", "age": "18"}'
#
# # 转换
# print("转换之前字符类型", type(data2))
# d3 = json.loads(data2)
# print("转换之后的字符类型", type(d3))



"""
    目标：写入json
    案例：
        1, data = {"name": "tom", "age": "12"}
        2, data = {"name": "李四", "age": ""23}
    操作：
    1, 导包 json
    2, 方法dump(写什么内容，往哪里写)
    注意：
        1，写入操作 w
        2，写入方法：dump()而不是dumps()
"""

# data3 = {"name": "李二狗", "age": "24"}
#
# with open("./write.json", "w", encoding="utf-8") as g:
#     json.dump(data3, g, ensure_ascii=False)


"""
    目标：读取json
    案例：
        读取write.json
    操作：
    1, 导包 json
    2, 方法load(文件流)
    注意：
        1，写入操作 r
        2，写入方法：load()而不是loads()
"""

with open("./write.json", encoding="utf-8") as r:
    data4 = json.load(r)
    print(data4)
    print(type(data4))