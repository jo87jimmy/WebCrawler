# Bopomofo MP3 Web Crawler

這是一個用於從抓取注音符號教學 MP3 檔案的 Python 爬蟲。

## 功能特點
- 自動抓取指定頁面中的所有注音 MP3 連結。
- 模擬瀏覽器標頭 (User-Agent) 以避免被伺服器阻擋 (403 Forbidden)。
- 自動建立下載目錄並儲存檔案。
- 具有下載進度提示。

## 專案結構
```text
WebCrawler/
├── crawler.py          # 爬蟲主程式
├── requirements.txt    # 必要的 Python 套件列表
├── README.md           # 專案說明文件
└── downloads/          # (自動生成) 存放下載的 MP3 檔案
```

## 安裝與執行

### 1. 準備環境
確保你的電腦已安裝 Python 3.x。

### 2. 安裝套件
在終端機 (Terminal/PowerShell) 中執行以下指令：
```bash
pip install -r requirements.txt
```

### 3. 執行爬蟲
執行以下指令開始下載：
```bash
python crawler.py
```
```
python download_mdn.py
```
## 注意事項
- 請確保網路連線正常。
- 程式內建了 0.5 秒的請求間隔，以減輕對目標伺服器的負擔，這是一個良好的爬蟲習慣。
- 下載的檔案將會直接存放在 `downloads` 資料夾中。

##僅供學術研究使用，請勿用於商業用途。
