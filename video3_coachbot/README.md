## 簡介

這個項目展示了如何將ChatGPT轉化為你的私人領導力教練。我們將利用Python程式碼和OpenAI API，讓ChatGPT扮演領導力教練的角色，並結合Gradio來提供更好的用戶體驗。此外，我們將介紹如何進行token計數以及異常處理。

具體的，我們將介紹三個Python檔案：

1. **"CoachBotBasic.py"**: 此檔案展示了基本的AI教練設置，ChatGPT將根據用戶的問題提供相對應的回答。
2. **"CoachBotHist.py"**: 此檔案添加了聊天歷史的功能，使得用戶可以查看與AI教練的過往對話。
3. **"CoachBotToken.py"**: 此檔案展示了如何檢查和處理token的數量，以防止超過OpenAI API的最大限制。

## Prerequisites

在執行這些範例程式碼之前，你需要準備以下的項目：

1. Python 3.6或以上的版本。
2. 安裝所需的Python函式庫：`openai`, `gradio`, `tiktoken`。
3. OpenAI API密鑰，這可以從OpenAI官方網站申請得到。

請記得在運行程式碼之前設定你的OpenAI API密鑰，並確保你已經安裝了所有必須的函式庫。

## 設定


1. 首先，你需要確保已經安裝了所需的Python函式庫。如果還未安裝，可以運行下列命令來安裝：

    ```shell
    pip install openai gradio tiktoken
    ```
2. 設定OpenAI API金鑰的環境變數：
    在 Windows 系統下設定環境變數的方法如下：

    - 按下 `Windows鍵+X`，並點擊 `系統`。
    - 點擊 `進階系統設定`。
    - 在系統內容對話框中，點擊 `進階` 標籤頁，然後點擊 `環境變數`。
    - 在環境變數對話框中，點擊 `新建`（在用戶變數或系統變數部分，取決於您希望這些變數是否應用於所有使用者）。
    - 輸入變數名稱（例如：`OPENAI_API_KEY`）以及變數值（您的OpenAI API金鑰）。然後，點擊 `確定`。

    完成以上步驟後，您必須重新啟動電腦，使這些變數生效。這些環境變數將在每次啟動時自動設定，並可供您的 Python 程式使用。


## 運行

每個Python檔案都可以獨立運行。例如，如果你想運行"CoachBotBasic.py"，你可以在命令列中輸入：

```bash
python CoachBotBasic.py
```

這將會啟動Gradio界面，你可以在網頁中與AI教練進行對話。

