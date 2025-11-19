def get_lucky_color(birth: str):
    """birth格式: YYYY-MM-DD HH"""
    # 示例：1990-05-01 14:00 → 1990年5月1日14点
    # 正确解析日期字符串
    try:
        date_part, hour = birth.split(" ")
        year, month, day = map(int, date_part.split('-'))
        hour = int(hour.split(':')[0])
        
        # 简化版幸运色计算（避免依赖pybazi库）
        # 根据出生月份确定幸运色
        month_colors = {
            1: "红色", 2: "橙色", 3: "黄色", 4: "绿色",
            5: "青色", 6: "蓝色", 7: "紫色", 8: "粉色",
            9: "棕色", 10: "灰色", 11: "黑色", 12: "白色"
        }
        return month_colors.get(month, "紫色")  # 默认紫色
    except Exception as e:
        # 如果解析失败，返回默认颜色
        return "紫色"