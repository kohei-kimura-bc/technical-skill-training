import json

try:
    invalid_json_string = '{"name": "Alice", "age": 30'  # 閉じカッコが不足
    data = json.loads(invalid_json_string)
except json.JSONDecodeError as e:
    print(f"JSON Decode Error: {e}")
