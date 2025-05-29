import json

# リスト型のデータ
data = ["apple", "banana", "cherry"]
print("成型前のデータは", data)
print("成型前のデータタイプは", type(data))

# リストをJSON形式の文字列に変換
json_string = json.dumps(data)

print("JSONへdumpした後のデータは", json_string)  # 出力: ["apple", "banana", "cherry"]
print("JSONへdumpした後のデータタイプは", type(json_string))

loaded_data = json.loads(json_string)
print("JSONからloadした後のデータは", loaded_data)
print("JSONからloadした後のデータタイプは", type(loaded_data))
