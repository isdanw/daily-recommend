def recommend_outfit(weather_data: dict, lucky_color: str):
    temp = int(weather_data["temperature"])
    weather = weather_data["weather"]
    
    # 基础穿搭规则
    if temp > 25:
        base = "短袖 + 短裤"
    elif 15 <= temp <= 25:
        base = "长袖衬衫 + 薄外套"
    elif 5 <= temp < 15:
        base = "毛衣 + 轻薄外套"
    else:
        base = "厚外套 + 围巾"
    
    # 添加幸运色
    return f"今日推荐：{lucky_color}色 {base}（适合{weather}）"