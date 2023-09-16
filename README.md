# 訂餐平台
這是一個用於統計班上同學訂餐的網站，使用簡單的前端搭配輕量級框架*Flask*。

## 安裝
此專案需要*Python*、*pip*、*Flask*，使用前請先安裝。
以下為*Linux*安裝方法：
```
sudo apt install python3
sudo apt install python3-pip
pip install flask
```

## 使用方法
使用前請先設定網路，預設使用port=5000。
移動至檔案所在目錄，並執行*Python*主程式
```
cd ./api/
flask run --app main.py
```

## 架構
group_order
- api
   - static:CSS等靜態檔案
   - templates：html檔案

## 特色
使用簡單的前端*HTML*及*CSS*，配合後端輕量級*Python*框架*Flask*，大小輕盈也可以架設於雲端伺服器

## 待實作功能
1. 自動統計各餐點數量及總價
2. 於每日設定時間清除過期訂購列表
3. 於設定時間關閉訂餐功能

## 技術指標
![Static Badge](https://img.shields.io/badge/-python?logo=Python&label=Python) ![Static Badge](https://img.shields.io/badge/-Flask?logo=Flask&label=Flask) ![Static Badge](https://img.shields.io/badge/-HTML?logo=Html5&label=HTML) ![Static Badge](https://img.shields.io/badge/-CSS?logo=CSS3&label=CSS)
