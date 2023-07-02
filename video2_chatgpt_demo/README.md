# 語音識別天氣機器人

## 簡介

這個項目是一個語音識別天氣機器人，它接收用戶的中文語音輸入，使用OpenAI的ChatGPT處理，並提供指定位置的當前天氣信息。該機器人使用OpenWeatherMap API來獲取天氣數據。

## Prerequisites

- Python 3.6或更高版本。
- 以下Python套件：
  - `openai`
  - `gradio`
  - `speech_recognition`
  - `requests`
- OpenAI API金鑰。
- OpenWeatherMap API金鑰。

## 設定

4. 設定OpenAI API金鑰和OpenWeatherMap API金鑰的環境變數：

    在 Windows 系統下設定環境變數的方法如下：

    - 按下 `Windows鍵+X`，並點擊 `系統`。
    - 點擊 `進階系統設定`。
    - 在系統內容對話框中，點擊 `進階` 標籤頁，然後點擊 `環境變數`。
    - 在環境變數對話框中，點擊 `新建`（在用戶變數或系統變數部分，取決於您希望這些變數是否應用於所有使用者）。
    - 輸入變數名稱（例如：`OPENAI_API_KEY`）以及變數值（您的OpenAI API金鑰）。然後，點擊 `確定`。
    - 重複步驟4和步驟5，為 OpenWeatherMap API 金鑰建立另一個環境變數（例如：`WEATHER_API_KEY`）。

    完成以上步驟後，您必須重新啟動電腦，使這些變數生效。這些環境變數將在每次啟動時自動設定，並可供您的 Python 程式使用。

## 運行

在終端機中執行以下命令以開始應用程式：
```bash
python chatgpt_demo.py
```

## 使用

啟動應用程式後，點擊界面上的 "Record" 按鈕開始錄音，並說出您想獲取天氣信息的地點。機器人將處理您的語音輸入，提取地點信息，並提供該地的當前天氣信息。


