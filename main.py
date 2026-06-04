#!/usr/bin/env python3
"""
SEO 工厂 v5.0 - 最终版 (路由优先级修复)
"""
import asyncio, json, os, random, re
from pathlib import Path
from datetime import datetime as dt
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx

BASE = Path.home() / "WorkBuddy" / "SEO"
DOCS = BASE / "docs"
DOCS.mkdir(exist_ok=True)

NIM_API_KEY = os.getenv("NVIDIA_API_KEY", "")
if not NIM_API_KEY:
    env_file = Path.home() / ".hermes" / ".env"
    if env_file.exists():
        content = env_file.read_text()
        match = re.search(r'NVIDIA_API_KEY["\s:=]+["\']?([^"\'\s]+)', content)
        if match: NIM_API_KEY = match.group(1)

BASE_URL = "https://integrate.api.nvidia.com/v1"
MODEL = "nvidia/nemotron-4-340b-instruct"
USE_REAL_AI = bool(NIM_API_KEY)

if not USE_REAL_AI:
    print("⚠️ 警告：NVIDIA_API_KEY 未找到！将使用伪生成模式 (本地模拟 AI)。")
else:
    print("✅ 已加载 NVIDIA_API_KEY。真实 AI 模式已启用。")

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

INDEX_HTML = (DOCS / "index.html").read_text(encoding="utf-8")

# --- 1. 首页 ---
@app.get("/", response_class=HTMLResponse)
async def root():
    return INDEX_HTML

# --- 2. API: AI 生成 (明确定义) ---
@app.post("/api/generate")
async def api_generate(topic: str = Query(...)):
    if USE_REAL_AI:
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(
                    f"{BASE_URL}/chat/completions",
                    headers={"Authorization": f"Bearer {NIM_API_KEY}", "Content-Type": "application/json"},
                    json={"model": MODEL, "messages": [{"role": "user", "content": f"用 3 句话深度解析 '{topic}'，风格：赛博朋克，硬核技术。"}], "temperature": 0.7},
                    timeout=30
                )
                content = resp.json()["choices"][0]["message"]["content"] if resp.status_code == 200 else f"[API 错误 {resp.status_code}]"
        except Exception as e:
            content = f"[系统错误] {e}"
    else:
        await asyncio.sleep(0.5)
        content = f"[模拟生成] '{topic}' 是当前最危险的量子现象。"

    slug = re.sub(r'[<>:"/\\|?*]', '', topic)[:30].replace(' ', '-') or "untitled"
    filename = f"generated_{slug}.html"
    filepath = DOCS / filename
    html = f"""
    <!DOCTYPE html><html><head><meta charset="UTF-8"><title>{topic} v5.0</title>
    <style>body{{font-family:monospace;background:#000;color:#0ff;padding:40px}}h1{{color:#f0f}} a{{color:#0ff}}</style></head>
    <body><h1>REAL GENERATION: {topic}</h1><p>{content}</p><br><a href="/">← 返回</a></body></html>
    """
    with open(filepath, "w", encoding="utf-8") as f: f.write(html)
    return JSONResponse(content={"status": "success", "filename": filename, "url": f"/{filename}"})

# --- 3. 文章页面 (通配符路由，排除 /api/) ---
@app.get("/{filename}", response_class=HTMLResponse)
async def get_article(filename: str):
    if filename.startswith("api/"):
        raise HTTPException(status_code=404, detail="Not Found")
    file_path = DOCS / filename
    if file_path.exists():
        return file_path.read_text(encoding="utf-8")
    return HTMLResponse(content="<h1>404</h1>", status_code=404)

# --- 4. WebSocket ---
class Pool:
    def __init__(self): self.conns = []
    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.conns.append(ws)
    def disconnect(self, ws: WebSocket):
        if ws in self.conns: self.conns.remove(ws)
    async def broadcast(self, msg: dict):
        for c in self.conns:
            try: await c.send_json(msg)
            except: pass

pool = Pool()

@app.websocket("/ws")
async def ws(ws: WebSocket):
    await pool.connect(ws)
    try:
        while True:
            await asyncio.sleep(3)
            await pool.broadcast({"type": "heartbeat", "latency": f"{random.randint(1,20)}ms", "nodes": random.randint(4000,5000), "new_topic": random.choice(["量子","神经","意识"]), "entropy": random.randint(10,50)})
    except:
        pool.disconnect(ws)

if __name__ == "__main__":
    import uvicorn
    print(f"🚀 v5.0 最终版启动 | AI: {'Real' if USE_REAL_AI else 'Fake'}")
    uvicorn.run(app, host="0.0.0.0", port=8080)