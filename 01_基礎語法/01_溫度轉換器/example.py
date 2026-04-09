# 溫度轉換器示例代碼

# 範例1：簡單的攝氏度轉華氏度
print("=== 範例1：簡單轉換 ===")
celsius = float(input("請輸入攝氏度溫度："))
fahrenheit = celsius * 9/5 + 32
print(f"攝氏度 {celsius}°C 等於華氏度 {fahrenheit}°F")

# 範例2：華氏度轉攝氏度
print("\n=== 範例2：華氏度轉攝氏度 ===")
fahrenheit_input = float(input("請輸入華氏度溫度："))
celsius_output = (fahrenheit_input - 32) * 5/9
print(f"華氏度 {fahrenheit_input}°F 等於攝氏度 {celsius_output:.2f}°C")

# 範例3：互動式溫度轉換器
print("\n=== 範例3：互動式轉換器 ===")
print("請選擇轉換方向：")
print("1. 攝氏度 → 華氏度")
print("2. 華氏度 → 攝氏度")

choice = input("請選擇 (1 或 2)：")

if choice == "1":
    temp = float(input("請輸入攝氏度："))
    result = temp * 9/5 + 32
    print(f"結果：{temp}°C = {result:.2f}°F")
elif choice == "2":
    temp = float(input("請輸入華氏度："))
    result = (temp - 32) * 5/9
    print(f"結果：{temp}°F = {result:.2f}°C")
else:
    print("無效的選擇！")
