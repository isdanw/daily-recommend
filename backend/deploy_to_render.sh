#!/bin/bash
# deploy_to_render.sh

# 检查是否在 backend 目录
if [ ! -f "main.py" ]; then
  echo "Error: Run this script from the backend directory!"
  exit 1
fi

# 1. 生成 requirements.txt
echo "fastapi" > requirements.txt
echo "uvicorn" >> requirements.txt
echo "aiohttp" >> requirements.txt
echo "python-multipart" >> requirements.txt

# 2. 生成 Procfile
echo "web: uvicorn main:app --host 0.0.0.0 --port \$PORT" > Procfile

# 3. 修改 main.py 使用环境变量
if ! grep -q "import os" main.py; then
  sed -i '1iimport os' main.py
fi

# 确保已经导入os模块
if ! grep -q "import os" main.py; then
  sed -i '1iimport os' main.py
fi

# 检查是否已经更新API密钥处理
if ! grep -q "os.getenv" main.py; then
  echo "Warning: API key handling not updated correctly"
fi

echo -e "\n✅ 部署配置已生成:"
echo "  • requirements.txt: $(cat requirements.txt | tr '\n' ' ')"
echo "  • Procfile: $(cat Procfile)"
echo -e "\n⚠️ 请手动完成："
echo "  1. 在 Render.com 设置环境变量 QWEATHER_API_KEY"
echo "  2. 推送代码到 GitHub"
echo "  3. 通过 Render.com 部署 GitHub 仓库"