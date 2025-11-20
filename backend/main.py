import os
import sys
import inspect
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

# 添加当前目录到sys.path以便正确导入模块
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, currentdir)

# 使用绝对导入替代相对导入
from weather import get_weather
from fortune import get_lucky_color
from outfit import recommend_outfit
from diet import recommend_diet
from image import generate_outfit_image

app = FastAPI()

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 用户数据模型
class User(BaseModel):
    name: str
    birth: str  # 格式: YYYY-MM-DD HH
    city: str
    diet_pref: str
    style_pref: str

@app.post("/register")
async def register_user(user: User):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, birth TEXT, city TEXT, diet_pref TEXT, style_pref TEXT)")
    c.execute("INSERT INTO users (name, birth, city, diet_pref, style_pref) VALUES (?, ?, ?, ?, ?)", 
              (user.name, user.birth, user.city, user.diet_pref, user.style_pref))
    conn.commit()
    return {"status": "success", "user_id": c.lastrowid}

@app.get("/weather/{city}")
async def get_city_weather(city: str):
    api_key = os.getenv("QWEATHER_API_KEY")
    # 即使没有API密钥也继续执行，让weather模块处理
    return await get_weather(city, api_key or "")

@app.get("/fortune/{user_id}")
async def get_fortune(user_id: int):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT birth FROM users WHERE id=?", (user_id,))
    result = c.fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    birth = result[0]
    
    lucky_color = get_lucky_color(birth)
    # 模拟运势描述（后续用Qwen生成）
    return {
        "lucky_color": lucky_color,
        "wealth": "财运平稳，可小额投资",
        "love": "社交运佳，易遇新朋友"
    }

@app.get("/outfit/{user_id}")
async def get_outfit(user_id: int):
    # 1. 获取用户信息
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT birth, city FROM users WHERE id=?", (user_id,))
    result = c.fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    birth, city = result
    
    # 2. 获取天气
    api_key = os.getenv("QWEATHER_API_KEY")
    # 即使没有API密钥也继续执行，让weather模块处理
    weather = await get_weather(city, api_key or "")
    
    # 3. 获取运势（幸运色）
    fortune = await get_fortune(user_id)
    
    # 4. 生成穿搭
    outfit = recommend_outfit(weather, fortune["lucky_color"])
    return {"outfit": outfit}

@app.get("/diet/{user_id}")
async def get_diet(user_id: int):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT diet_pref, city FROM users WHERE id=?", (user_id,))
    result = c.fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    diet_pref, city = result
    
    api_key = os.getenv("QWEATHER_API_KEY")
    # 即使没有API密钥也继续执行，让weather模块处理
    weather = await get_weather(city, api_key or "")
    return {"diet": recommend_diet(diet_pref, weather["weather"])}

@app.get("/outfit-image/{user_id}")
async def get_outfit_image(user_id: int):
    # 获取用户所在城市
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT city FROM users WHERE id=?", (user_id,))
    result = c.fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    city = result[0]
    
    fortune = await get_fortune(user_id)
    
    api_key = os.getenv("QWEATHER_API_KEY")
    # 即使没有API密钥也继续执行，让weather模块处理
    weather_data = await get_weather(city, api_key or "")
    image_url = generate_outfit_image(fortune["lucky_color"], weather_data["weather"])
    return {"image_url": image_url}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)