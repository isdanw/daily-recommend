def recommend_diet(user_pref: str, weather: str):
    # 简化规则：根据天气和季节（假设11月=冬季）
    if "干燥" in weather:
        base = "银耳羹 + 梨"
    elif "雨" in weather:
        base = "姜汤 + 热粥"
    else:
        base = "蔬菜汤"
    
    # 过滤用户偏好
    if "忌辣" in user_pref:
        base += "（微辣版）"
    if "素食" in user_pref:
        base += "（素菜版）"
    
    return f"推荐：{base}（润燥养生）"