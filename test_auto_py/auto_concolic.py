import subprocess
import time

api = "/goform/setUsbUnload"


# 啟動 ac15_httpd_concolic.py 腳本，並獲取輸出
process = subprocess.Popen(["python", "/home/hsu/Concolic_Project/avatar_project/ac15_httpd_concolic.py"], stdout=subprocess.PIPE)

# 讀取輸出並檢查是否為 "start concrete"
while True:
    output = process.stdout.readline().decode().strip()
    print(output)  # 打印輸出
    if output == "[*] start concrete":
        # 輸出為 "start concrete"，等待 5 秒
        time.sleep(5)
        # 執行 get.py 腳本
        subprocess.call(["python", "/home/hsu/Concolic_Project/avatar_project/api_request.py", api])

    if output == "finish angr":
        break
