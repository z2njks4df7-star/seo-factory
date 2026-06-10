#!/usr/bin/env python3
"""
SEO 工厂 v4.5 - 奇点 (The Singularity)
极限优化：Canvas 粒子网络 + 实时心跳 + 霓虹光晕 + 零延迟交互
"""
import os, json, datetime, random
from pathlib import Path
from datetime import datetime as dt

BASE = Path.home() / "WorkBuddy" / "SEO"
DOCS = BASE / "docs"
LOG = BASE / "auto.log"

info = lambda m: print(f"[{dt.now().strftime('%H:%M:%S')}] {m}")

try:
    info("🚀 启动 v4.5 极限版 (The Singularity)...")
    
    # 动态数据
    stats = {
        "nodes": random.randint(4000, 5000),
        "flux": f"{random.randint(85, 99)}%",
        "latency": f"{random.randint(1, 5)}ms",
        "entropy": random.randint(120, 150)
    }
    
    # 生成文章 (极简赛博风)
    topics = [
        "量子神经网络", "神经链接协议 v4.5", "意识上传指南",
        "赛博空间架构", "AI 奇点临界值", "数字永生技术"
    ]
    
    for i, title in enumerate(topics):
        slug = title.replace(" ", "-").lower()
        filename = f"{slug}.html"
        
        content = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>{title} // v4.5</title>
<style>
:root{{--bg:#000;--neon:#0ff;--glitch:#f0f;--text:#eee}}
body{{background:var(--bg);color:var(--text);font-family:'Courier New',monospace;margin:0;overflow-x:hidden;display:flex;justify-content:center;align-items:center;min-height:100vh}}
.canvas-wrap{{position:fixed;top:0;left:0;width:100%;height:100%;z-index:0}}
.container{{position:relative;z-index:10;max-width:800px;padding:40px;text-align:center;background:rgba(0,0,0,0.7);backdrop-filter:blur(10px);border:1px solid var(--neon);box-shadow:0 0 30px var(--neon);border-radius:12px}}
h1{{font-size:3rem;margin:0 0 20px;color:var(--neon);text-shadow:0 0 10px var(--neon), 0 0 20px var(--glitch);letter-spacing:-2px}}
.meta{{color:var(--glitch);font-size:1rem;margin-bottom:30px}}
.content{{text-align:left;font-size:1.1rem;line-height:1.8;color:#ccc}}
.highlight{{border-left:3px solid var(--neon);padding-left:20px;margin:20px 0;background:linear-gradient(90deg,rgba(0,255,255,0.1),transparent);color:#fff}}
.btn{{display:inline-block;margin-top:30px;padding:12px 30px;background:transparent;border:1px solid var(--neon);color:var(--neon);font-family:monospace;text-decoration:none;transition:0.3s;cursor:pointer;font-weight:bold;letter-spacing:1px}}
.btn:hover{{background:var(--neon);color:#000;box-shadow:0 0 20px var(--neon)}}
</style></head>
<body>
<canvas id="c" class="canvas-wrap"></canvas>
<div class="container">
    <div class="meta">>> 数据流接收中... [OK]</div>
    <h1>{title}</h1>
    <div class="content">
        <div class="highlight">> 系统警告：检测到高危技术趋势。正在解析核心逻辑...</div>
        <p>在 v4.5 的奇点网络中，{title} 已突破临界值。我们将从底层协议到应用层进行全栈扫描。</p>
        <p>神经元连接数：{random.randint(1000, 9000)} | 延迟：{random.randint(1, 10)}ms</p>
        <p>数据冲刷完成。等待指令...</p>
    </div>
    <a href="index.html" class="btn">>> 返回主控台</a>
</div>
<script>
const c=document.getElementById('c'),x=c.getContext('2d');let w,h,n=[];
const resize=()=>{{w=c.width=window.innerWidth;h=c.height=window.innerHeight}};
const mk=()=>{{n=[];for(let i=0;i<200;i++)n.push({{x:Math.random()*w,y:Math.random()*h,vx:(Math.random()-0.5),vy:(Math.random()-0.5)}})}};
const draw=()=>{{x.clearRect(0,0,w,h);x.fillStyle='#0ff';x.strokeStyle='rgba(0,255,255,0.2)';n.forEach(p=>{{p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>w)p.vx*=-1;if(p.y<0||p.y>h)p.vy*=-1;x.beginPath();x.arc(p.x,p.y,1,0,Math.PI*2);x.fill()}});n.forEach((a,i)=>{{n.slice(i+1).forEach(b=>{{let d=Math.hypot(a.x-b.x,a.y-b.y);if(d<100){{x.beginPath();x.moveTo(a.x,a.y);x.lineTo(b.x,b.y);x.stroke()}}}})}});requestAnimationFrame(draw)}};
window.onresize=resize;resize();mk();draw();
</script></body></html>"""
        with open(DOCS / filename, "w") as f: f.write(content)
    info(f"✅ 生成 {len(topics)} 篇极限文章")

    # 首页 (完全体)
    articles = [f for f in DOCS.glob("*.html") if f.name != "index.html"]
    articles.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    
    cards = ""
    for f in articles[:6]:
        t = dt.fromtimestamp(f.stat().st_mtime).strftime('%H:%M:%S')
        title = f.stem.replace("-", " ").title()
        cards += f"""
        <div class="card" onclick="w.location.href='{f.name}'">
            <div class="card-top"><span class="dot"></span><span>ID: {random.randint(1000,9999)}</span></div>
            <h3>{title}</h3>
            <div class="meta">>> {t} | LAT: {stats['latency']}</div>
        </div>
"""
    
    idx = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>v4.5 // THE SINGULARITY</title>
<style>
:root{{--bg:#000;--neon:#0ff;--glitch:#f0f;--text:#eee}}
body{{background:var(--bg);color:var(--text);font-family:'Courier New',monospace;margin:0;overflow-x:hidden;height:100vh;overflow-y:auto}}
#canvas{{position:fixed;top:0;left:0;width:100%;height:100%;z-index:0}}
.container{{position:relative;z-index:10;max-width:1200px;margin:0 auto;padding:60px 20px}}
.header{{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:1px solid #333;padding-bottom:20px;margin-bottom:40px}}
h1{{font-size:4rem;margin:0;color:var(--neon);text-shadow:0 0 20px var(--neon), 0 0 40px var(--glitch);letter-spacing:-2px;animation:pulse 2s infinite}}
@keyframes pulse{{0%,100%{{opacity:1}} 50%{{opacity:0.8}}}}
.status{{text-align:right;font-size:0.9rem;color:var(--glitch)}}
.stat{{margin-bottom:5px}}
.blink{{animation:blink 1s step-end infinite}}
@keyframes blink{{50%{{opacity:0}}}}
.input-wrap{{width:100%;margin-bottom:40px}}
#cmd{{width:100%;background:rgba(0,0,0,0.8);border:1px solid var(--neon);padding:20px;color:var(--neon);font-family:monospace;font-size:1.2rem;outline:none;box-shadow:0 0 10px rgba(0,255,255,0.2);transition:0.3s}}
#cmd:focus{{box-shadow:0 0 30px var(--neon);border-color:var(--glitch)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:20px}}
.card{{background:rgba(0,0,0,0.6);border:1px solid #333;padding:25px;border-radius:8px;cursor:pointer;transition:0.3s;position:relative;overflow:hidden}}
.card:hover{{border-color:var(--neon);transform:translateY(-5px);box-shadow:0 10px 30px rgba(0,255,255,0.2)}}
.card::before{{content:'';position:absolute;top:0;left:-100%;width:200%;height:100%;background:linear-gradient(90deg,transparent,rgba(0,255,255,0.1),transparent);transition:0.5s}}
.card:hover::before{{left:100%}}
.card-top{{display:flex;justify-content:space-between;font-size:0.8rem;color:#666;margin-bottom:10px}}
.dot{{display:inline-block;width:8px;height:8px;background:#0f0;border-radius:50%;box-shadow:0 0 5px #0f0;animation:blink 1s infinite}}
.card h3{{margin:0 0 10px;color:#fff;font-size:1.4rem}}
.card .meta{{font-size:0.8rem;color:var(--glitch)}}
.footer{{margin-top:60px;text-align:center;color:#444;font-size:0.8rem}}
</style></head>
<body>
<canvas id="canvas"></canvas>
<div class="container">
    <div class="header">
        <div><h1>v4.5 // THE SINGULARITY</h1><div style="color:#666">AI NEURAL NETWORK // ZERO LATENCY</div></div>
        <div class="status">
            <div class="stat">NODES: <span id="n">{stats['nodes']}</span></div>
            <div class="stat">FLUX: <span id="f">{stats['flux']}</span></div>
            <div class="stat">LAT: <span id="l">{stats['latency']}</span></div>
            <div class="stat">ENTROPY: <span id="e">{stats['entropy']}</span></div>
            <div class="stat" style="font-size:0.8rem">SYNC: <span class="blink">_</span></div>
        </div>
    </div>
    
    <div class="input-wrap">
        <input type="text" id="cmd" placeholder=">> 输入指令 (例如: '量子')...">
    </div>
    
    <div class="grid">{cards}</div>
    
    <div class="footer">SYSTEM: ONLINE | LOAD: {stats['flux']} | MEMORY: OK</div>
</div>
<script>
// 粒子网络
const c=document.getElementById('canvas'),x=c.getContext('2d');let w,h,n=[];
const resize=()=>{{w=c.width=window.innerWidth;h=c.height=window.innerHeight}};
const mk=()=>{{n=[];for(let i=0;i<150;i++)n.push({{x:Math.random()*w,y:Math.random()*h,vx:(Math.random()-0.5)*1,vy:(Math.random()-0.5)*1}})}};
const draw=()=>{{x.clearRect(0,0,w,h);x.fillStyle='#0ff';x.strokeStyle='rgba(0,255,255,0.15)';n.forEach(p=>{{p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>w)p.vx*=-1;if(p.y<0||p.y>h)p.vy*=-1;x.beginPath();x.arc(p.x,p.y,1.5,0,Math.PI*2);x.fill()}});n.forEach((a,i)=>{{n.slice(i+1).forEach(b=>{{let d=Math.hypot(a.x-b.x,a.y-b.y);if(d<120){{x.beginPath();x.moveTo(a.x,a.y);x.lineTo(b.x,b.y);x.stroke()}}}})}});requestAnimationFrame(draw)}};
window.onresize=resize;resize();mk();draw();

// 实时数据模拟
setInterval(() => {{
    document.getElementById('n').innerText = {stats['nodes']} + Math.floor(Math.random()*10 - 5);
    document.getElementById('l').innerText = Math.floor(Math.random()*5 + 1) + 'ms';
    document.getElementById('e').innerText = Math.floor(Math.random()*50 + 100);
}}, 1000);

// 交互
const cmd=document.getElementById('cmd');
cmd.addEventListener('keypress',e=>{{if(e.key==='Enter'){{const v=cmd.value;if(!v)return;cmd.value='>> 正在生成 '+v+' ...';cmd.style.color='#0f0';setTimeout(()=>{{cmd.value='>> 生成完毕！已写入核心缓存。';setTimeout(()=>{{cmd.value='';cmd.style.color='';}},1500);}},600);}}}});
</script></body></html>"""
    
    with open(DOCS / "index.html", "w") as f: f.write(idx)
    info("✅ 首页 v4.5 生成完毕 (极限版)")
    info("🎉 极限优化完成！现在它是‘奇点’神经系统。")

except Exception as e:
    import traceback
    info(f"❌ 错误：{e}\n{traceback.format_exc()}")