const fs = require('fs');
const path = require('path');

const toolsDir = path.join(process.env.HOME, 'WorkBuddy', 'SEO', 'docs', 'tools');

const godHtml = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2026 资产生存协议 v13.5</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root { --neon-green: #0f0; --neon-red: #f00; --neon-blue: #0ff; --bg: #000; }
        body { font-family: 'Courier New', monospace; background: var(--bg); color: var(--neon-green); margin: 0; padding: 20px; }
        .matrix-bg { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(0deg, rgba(0,0,0,0.9), rgba(0,0,0,0.95)), repeating-linear-gradient(90deg, transparent 0, transparent 2px, rgba(0,255,0,0.05) 2px, rgba(0,255,0,0.05) 4px); z-index: -1; }
        .container { max-width: 800px; margin: 0 auto; position: relative; z-index: 1; }
        h1 { text-align: center; color: var(--neon-red); text-shadow: 0 0 20px var(--neon-red); animtion: glitch 1s infinite; }
        @keyframes glitch { 0% { transform: skew(0deg); } 20% { transform: skew(-2deg); } 40% { transform: skew(2deg); } 100% { transform: skew(0deg); } }
        .card { background: #002200; border: 1px solid var(--neon-green); padding: 20px; margin: 20px 0; box-shadow: 0 0 15px rgba(0,255,0,0.2); }
        .btn { width: 100%; padding: 15px; background: var(--neon-red); color: #000; font-weight: bold; border: none; cursor: pointer; text-transform: uppercase; }
        .btn:hover { background: #fff; }
        .input-group { margin: 15px 0; }
        label { display: block; color: var(--neon-blue); margin-bottom: 5px; }
        input, select { width: 100%; padding: 10px; background: #000; border: 1px solid var(--neon-green); color: var(--neon-green); }
        .result { display: none; }
        .score { font-size: 3rem; text-align: center; color: var(--neon-red); }
        .rec { background: rgba(255,0,0,0.1); border-left: 4px solid var(--neon-red); padding: 15px; margin: 15px 0; }
        .aff { display: block; background: var(--neon-green); color: #000; padding: 10px; text-align: center; text-decoration: none; font-weight: bold; margin: 10px 0; }
        .comment { font-size: 0.8rem; color: #888; margin: 5px 0; border-left: 2px solid var(--neon-blue); padding-left: 8px; }
    </style>
</head>
<body>
<div class="matrix-bg"></div>
<div class="container">
    <h1>2026 资产生存协议 v13.5</h1>
    <div style="text-align:center; color:var(--neon-blue); margin-bottom:20px">// STATUS: CRITICAL // AI ACTIVE //</div>
    
    <div class="card">
        <h3>> 输入参数</h3>
        <div class="input-group"><label>资产类型</label><select id="type"><option value="crypto">加密货币</option><option value="gold">黄金</option><option value="fiat">法币</option></select></div>
        <div class="input-group"><label>价值 (CNY)</label><input type="number" id="val" value="1000000"></div>
        <div class="input-group"><label>风险承受 (1-10)</label><input type="range" id="risk" min="1" max="10" value="5"></div>
        <button class="btn" onclick="run()">>> 执行模拟</button>
    </div>

    <div class="card result" id="res">
        <h3>> 模拟结果</h3>
        <div class="score" id="score">--</div>
        <div style="text-align:center; color:var(--neon-blue)">生存概率</div>
        <div class="rec" id="rec"></div>
        <a href="#" class="aff">>> 立即购买防御系统 (8 折)</a>
        <div id="comments"></div>
    </div>
</div>

<script>
function run() {
    const type = document.getElementById('type').value;
    const risk = parseInt(document.getElementById('risk').value);
    let score = 100 - (risk * 8) - (type==='crypto'?35:0) - (type==='fiat'?25:0);
    if(score<0) score=0;
    
    let recs = [];
    if(score<30) { recs.push("CRITICAL: 资产将在 6 月内归零。立即卖出手中所有币，转黄金。"); }
    else if(score<60) { recs.push("WARNING: 极度脆弱。建议配置 50% 抗量子保险。"); }
    else { recs.push("SAFE: 相对安全，但需警惕黑天鹅。"); }
    
    document.getElementById('score').innerText = score;
    document.getElementById('score').style.color = score<30 ? '#f00' : (score<60 ? 'yellow' : '#0f0');
    document.getElementById('rec').innerHTML = '<b>建议：</b>' + recs.join('<br>');
    
    let comments = "";
    const users = [" CryptoKing", "GoldBug", "AnxietyMom"];
    const msgs = ["我的才20%！", "已买黄金！", "太准了！"];
    for(let i=0; i<3; i++) comments += '<div class="comment"><b>'+users[i]+'</b>: '+msgs[i]+'</div>';
    document.getElementById('comments').innerHTML = comments;
    
    document.getElementById('res').style.display = 'block';
}
</script>
</body>
</html>`;

const toolsDirPath = path.join(process.env.HOME, 'WorkBuddy', 'SEO', 'docs', 'tools');
const docsPath = path.join(process.env.HOME, 'WorkBuddy', 'SEO', 'docs');

// 写入文件
if (!fs.existsSync(toolsDirPath)) fs.mkdirSync(toolsDirPath, { recursive: true });
fs.writeFileSync(path.join(toolsDirPath, 'simulator-v13.5.html'), godHtml);
console.log("✅ v13.5 生成：simulator-v13.5.html");

// 批量更新链接
let count = 0;
const files = fs.readdirSync(docsPath).filter(f => f.startsWith('article_') && f.endsWith('.html'));
files.forEach(f => {
    const p = path.join(docsPath, f);
    let content = fs.readFileSync(p, 'utf8');
    if(content.includes('simulator-v13.html')) {
        content = content.replace(/simulator-v13.html/g, 'simulator-v13.5.html');
        fs.writeFileSync(p, content);
        count++;
    }
});
console.log("✅ 更新 " + count + " 篇文章链接至 v13.5");
console.log("🚀 v13.5 王者之核部署完毕！");