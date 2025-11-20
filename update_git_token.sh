#!/bin/bash

echo "=== 更新GitHub个人访问令牌 ==="
echo ""

# 获取GitHub用户名
read -p "请输入你的GitHub用户名: " username

# 获取个人访问令牌
echo ""
echo "请在GitHub上生成个人访问令牌:"
echo "1. 访问 https://github.com/settings/tokens"
echo "2. 点击 'Generate new token' (Classic)"
echo "3. 给令牌起个名字，比如 'daily-recommend'"
echo "4. 选择 'repo' 权限范围"
echo "5. 点击 'Generate token'"
echo "6. 复制生成的令牌"
echo ""
read -sp "请输入你的GitHub个人访问令牌: " token
echo ""
echo ""

# 验证输入不为空
if [ -z "$username" ] || [ -z "$token" ]; then
    echo "错误: 用户名和令牌都不能为空!"
    exit 1
fi

# 更新远程URL
echo "正在更新远程仓库URL..."
git remote set-url origin https://$username:$token@github.com/isdanw/daily-recommend.git

# 显示更新后的URL（隐藏令牌部分）
echo "远程URL已更新为: https://$username:***@github.com/isdanw/daily-recommend.git"

echo ""
echo "✅ Git身份验证已更新完成！"