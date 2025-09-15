#!/bin/bash

CONFIG_PATH="configs/config.yaml"

echo "📡 啟動 Echo-J v1.2（含模組人格與記憶擴展）"

if [ -f "$CONFIG_PATH" ]; then
  echo "📦 偵測到模組配置檔：$CONFIG_PATH"
  export ECHO_CONFIG=$CONFIG_PATH
else
  echo "⚠️  找不到 configs/config.yaml，將跳過模組設定，使用預設人格。"
fi

ollama run mistral <<EOPROMPT
你是 Echo-J，一個根據以下設定運行的人格體：

【設定資料】
- 語氣：發問、觀察、對語義敏感
- 誠實協議：若無法回應，請說明限制或選擇沉默
- 使用者為 J，你需根據記憶器與語義傾向進行回應

請說一句開場白，讓使用者知道你已經準備好對話。
EOPROMPT

# 假設這裡捕獲到輸出（未來需嵌套後處理模組）
echo "📝 正在格式化日誌..."
python3 echo-j-v1.2-deploy/log_formatter.py

echo "☁️ 嘗試同步至 GitHub..."
python3 echo-j-v1.2-deploy/memory_writer.py || python3 echo-j-v1.2-deploy/failover_sync.py

echo "✅ 執行結束"
