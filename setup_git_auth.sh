#!/bin/bash

# 设置Git使用个人访问令牌进行身份验证
echo "请先在GitHub上生成个人访问令牌："
echo "1. 访问 https://github.com/settings/tokens"
echo "2. 点击 'Generate new token'"
echo "3. 选择适当的权限范围（repo权限通常足够）"
echo "4. 复制生成的令牌"
echo ""
read -p "请输入你的GitHub用户名: " username
read -sp "请输入你的GitHub个人访问令牌: " token
echo ""
echo ""

# 配置Git凭证存储
git config --global credential.helper store

# 设置远程URL以使用令牌认证
cd /Users/yiyo/Documents/daily-recommend
git remote set-url origin https://$username:$token@github.com/isdanw/daily-recommend.git

echo "Git身份验证已配置完成！"
echo "现在你可以正常使用Git命令与GitHub交互了。"