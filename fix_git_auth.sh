#!/bin/bash

echo "=== GitHub Personal Access Token Setup ==="
echo ""

# 检查是否已经设置了凭证助手
credential_helper=$(git config --global credential.helper)
if [ "$credential_helper" != "store" ]; then
    echo "正在配置Git凭证存储..."
    git config --global credential.helper store
fi

# 获取GitHub用户名
read -p "请输入你的GitHub用户名: " username

# 获取个人访问令牌
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

# 测试连接
echo "正在测试连接..."
if git ls-remote origin > /dev/null 2>&1; then
    echo "✅ 连接成功!"
    echo ""
    echo "Git身份验证已配置完成！"
    echo "现在你可以正常使用Git命令与GitHub交互了。"
else
    echo "❌ 连接失败，请检查用户名和令牌是否正确。"
    echo "注意：令牌只能查看一次，请确保复制了正确的令牌。"
fi