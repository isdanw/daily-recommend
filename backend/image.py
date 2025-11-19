import os
import httpx

def generate_outfit_image(lucky_color: str, weather: str):
    # 通义万相API调用
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/image-generation/generation"
    api_key = os.getenv("DASHSCOPE_API_KEY")
    if not api_key:
        # 如果没有API密钥，返回默认图片URL
        return "https://via.placeholder.com/1024x1024.png?text=Outfit+Image"
    
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "wanx-v1",
        "prompt": f"A stylish person wearing {lucky_color} clothing, {weather} weather, realistic style",
        "n": 1,
        "size": "1024*1024"
    }
    
    try:
        response = httpx.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["output"]["results"][0]["url"]
    except Exception as e:
        # 如果API调用失败，返回默认图片URL
        return "https://via.placeholder.com/1024x1024.png?text=Outfit+Image+Error"