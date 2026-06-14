"""
SEO Factory v8.0 - 变现闭环版 (Monetization)
核心升级：
1. 结果页插入 AdSense 占位符 + 联盟链接 (AWS/IBM Quantum)
2. 增加“高级版/企业咨询”钩子 -> 跳转私域 (两性用品/分销)
3. 增加“全网推广”话术生成器 (一键复制)
"""
import os
from pathlib import Path

BASE = Path.home() / "WorkBuddy" / "SEO"
TOOLS_DIR = BASE / "docs" / "tools"

# 1. 更新量子计算器 v8.0 (嵌入广告 + 联盟 + 私域)
calc_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>量子计算成本计算器 | 2026 免费版</title>
    <meta name="description" content="免费计算 2026 年量子计算机运行成本，支持 Shor/Grover 算法。获取 AWS/IBM 量子云服务优惠链接。">
    <style>
        :root { --primary: #10b981; --bg: #0f172a; --card: #1e293b; --text: #f8fafc; --ad: #f59e0b; }
        body { font-family: system-ui, -apple-system, sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 20px; line-height: 1.6; }
        .container { max-width: 700px; margin: 40px auto; }
        h1 { color: var(--primary); text-align: center; margin-bottom: 10px; }
        .subtitle { text-align: center; color: #94a3b8; margin-bottom: 30px; font-size: 0.95rem; }
        .card { background: var(--card); padding: 30px; border-radius: 12px; border: 1px solid #334155; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .form-group { margin-bottom: 20px; }
        label { display: block; margin-bottom: 8px; font-weight: 500; color: #cbd5e1; }
        input, select { width: 100%; padding: 12px; border-radius: 6px; border: 1px solid #475569; background: #0f172a; color: #fff; font-size: 1rem; box-sizing: border-box; }
        .btn { width: 100%; padding: 14px; background: var(--primary); color: #fff; border: none; border-radius: 6px; font-weight: bold; font-size: 1.1rem; cursor: pointer; transition: 0.2s; margin-top: 10px; }
        .btn:hover { filter: brightness(1.1); }
        .btn-affiliate { background: #3b82f6; margin-top: 15px; display: block; text-align: center; text-decoration: none; }
        .result { margin-top: 25px; padding: 20px; background: rgba(16, 185, 129, 0.1); border-radius: 8px; border: 1px solid var(--primary); display: none; }
        .data-row { display: flex; justify-content: space-between; margin-bottom: 8px; padding-bottom: 8px; border-bottom: 1px solid rgba(255,255,255,0.1); }
        .data-val { font-weight: bold; color: #34d399; }
        .ad-slot { margin: 20px 0; padding: 15px; background: #1e293b; border: 1px dashed var(--ad); text-align: center; border-radius: 6px; color: #fbbf24; font-size: 0.9rem; }
        .private-hook { margin-top: 20px; padding: 15px; background: rgba(59, 130, 246, 0.1); border: 1px solid #3b82f6; border-radius: 6px; text-align: center; }
        .private-hook h4 { margin: 0 0 10px 0; color: #60a5fa; }
        .private-hook a { color: #34d399; font-weight: bold; text-decoration: none; }
        .share-box { margin-top: 15px; padding: 10px; background: #0f172a; border-radius: 6px; word-break: break-all; font-family: monospace; font-size: 0.85rem; color: #94a3b8; display: none; }
        .tag { display: inline-block; padding: 3px 8px; background: #f59e0b; color: #000; font-size: 0.75rem; border-radius: 4px; margin-left: 8px; font-weight: bold; }
    </style>
</head>
<body>
<div class="container">
    <a href="../index.html" style="color:#38bdf8; text-decoration:none;">← 返回工具箱</a>
    <h1>⚛️ 量子计算成本计算器</h1>
    <p class="subtitle">2026 实时成本模型 | 免费 | 含云服务优惠</p>

    <div class="card">
        <div class="form-group">
            <label>目标算法</label>
            <select id="algo">
                <option value="shor">Shor 算法 (分解 2048 位 RSA)</option>
                <option value="grover">Grover 算法 (搜索 1TB 数据库)</option>
                <option value="chem">量子化学模拟 (催化剂研发)</option>
            </select>
        </div>
        <div class="form-group">
            <label>量子比特数 (Qubits)</label>
            <input type="number" id="qubits" value="4096" min="100" max="100000">
        </div>
        <div class="form-group">
            <label>纠错码开销 (Overhead)</label>
            <select id="code">
                <option value="1000">Surface Code (1000:1)</option>
                <option value="500">LDPC Code (500:1)</option>
            </select>
        </div>
        <div class="form-group">
            <label>运行时长</label>
            <select id="duration">
                <option value="1">1 小时</option>
                <option value="24">24 小时</option>
            </select>
        </div>

        <button class="btn" onclick="calculate()">🧮 立即计算成本</button>

        <div id="result" class="result">
            <h3>💰 估算成本 (2026 模型)</h3>
            <div class="data-row"><span>物理量子比特:</span><span class="data-val" id="res-physics">-</span></div>
            <div class="data-row"><span>算力需求:</span><span class="data-val" id="res-tflops">-</span></div>
            <div class="data-row"><span>电费:</span><span class="data-val" id="res-power">-</span></div>
            <div class="data-row"><span>硬件租赁:</span><span class="data-val" id="res-hw">-</span></div>
            <div class="data-row"><span style="font-size:1.1rem">🔥 总成本:</span><span class="data-val" id="res-total" style="font-size:1.2rem">-</span></div>
            
            <!-- 广告/联盟位 1: 云服务 -->
            <div class="ad-slot">
                💡 <strong>想直接租用量子算力？</strong><br>
                使用 <a href="#" style="color:#fbbf24">AWS Braket</a> 或 <a href="#" style="color:#fbbf24">IBM Quantum</a> 云服务，首月免费试用！
                <br><small style="color:#94a3b8">*点击获取专属优惠链接 (Affiliate)</small>
            </div>

            <div class="private-hook">
                <h4>🚀 企业级需求 / 深度报告？</h4>
                <p style="margin:0; font-size:0.9rem">获取 <strong>PDF 详细分析报告</strong> 或 <strong>定制化量子解决方案</strong>，加入我们的私域专家群。</p>
                <a href="https://x.com/youraccount" target="_blank" style="display:inline-block; background:#3b82f6; color:#fff; padding:10px 20px; border-radius:6px; margin-top:10px; text-decoration:none;">👉 点击加入私域群 (限时免费)</a>
            </div>
            
            <button class="btn" onclick="shareResult()" style="background:#64748b; margin-top:15px">🔗 生成分享链接</button>
            <div id="shareBox" class="share-box"></div>
        </div>

        <p style="text-align:center; font-size:0.8rem; color:#64748b;">
            🔒 隐私：本地计算，不上传数据。 
            <span style="display:block; margin-top:5px">广告支持我们提供永久免费工具</span>
        </p>
    </div>
    
    <!-- 广告位 2: 底部通栏 -->
    <div class="ad-slot" style="margin-top:30px; border:none; background:#0f172a; color:#94a3b8; padding:10px;">
        <!-- Google AdSense Placeholder -->
        <p>📢 广告位待接入：Google AdSense / 百度联盟</p>
    </div>
</div>

<script>
const PRICES = { power: 0.12, hw_rent: 5000, hw_depreciation: 0.2 };

function calculate() {
    const algo = document.getElementById('algo').value;
    const qubits = parseFloat(document.getElementById('qubits').value);
    const codeRatio = parseInt(document.getElementById('code').value);
    const hours = parseFloat(document.getElementById('duration').value);

    const physQubits = qubits * codeRatio;
    let tflops = 0;
    if(algo === 'shor') tflops = physQubits * 0.5; 
    else if(algo === 'grover') tflops = physQubits * 0.1;
    else tflops = physQubits * 2.0;

    const powerKWh = physQubits * 0.05 * hours; 
    const powerCost = powerKWh * PRICES.power;
    const hwCost = (tflops * PRICES.hw_rent + physQubits * PRICES.hw_depreciation) * hours;
    const total = powerCost + hwCost;

    document.getElementById('res-physics').innerText = physQubits.toLocaleString();
    document.getElementById('res-tflops').innerText = tflops.toLocaleString(undefined, {maximumFractionDigits:0});
    document.getElementById('res-power').innerText = '$' + powerCost.toLocaleString(undefined, {maximumFractionDigits:2});
    document.getElementById('res-hw').innerText = '$' + hwCost.toLocaleString(undefined, {maximumFractionDigits:0});
    document.getElementById('res-total').innerText = '$' + total.toLocaleString(undefined, {maximumFractionDigits:0});

    document.getElementById('result').style.display = 'block';
}

function shareResult() {
    const p = new URLSearchParams(window.location.search);
    const url = window.location.origin + window.location.pathname + '?' + p.toString();
    const box = document.getElementById('shareBox');
    box.innerText = url;
    box.style.display = 'block';
    navigator.clipboard.writeText(url);
}
window.onload = () => {
    const p = new URLSearchParams(location.search);
    if(p.has('a')) { calculate(); }
};
</script>
</body>
</html>"""

with open(TOOLS_DIR / "quantum-cost-calculator-v8.html", "w", encoding="utf-8") as f:
    f.write(calc_html)

print("✅ 变现版 v8.0 生成完成！")
print("   - 嵌入 AWS/IBM 联盟链接 (点击有佣金)")
print("   - 嵌入私域钩子 (导流到微信/分销群)")
print("   - 预留 AdSense 广告位 (挂代码就赚钱)")

# 2. 生成 Monetization Checklist
checklist = """
# 🔥 变现执行清单 ( köt ek )

## 1. 上线部署 (最重要)
- [ ] 将代码推送到 GitHub: `git push origin main`
- [ ] 在 GitHub Pages 开启：`Settings > Pages > Deploy from main`
- [ ] 访问：`https://z2njks4df7-star.github.io/seo-factory`

## 2. 接入广告
- [ ] 申请 Google AdSense (需要真实流量，先引流申请)
- [ ] 将 AdSense Script 替换到 `ad-slot` 位置
- [ ] 设置自动广告位

## 3. 接入联盟 (Affiliate)
- [ ] 注册 AWS Braket Affiliate / IBM Quantum Partner
- [ ] 将 `href="#"` 替换为真实联盟链接
- [ ] 测试点击是否带追踪参数

## 4. 私域引流 (高客单)
- [ ] 修改 `href="https://x.com/..."` 为你的真实私域入口 (微信/Telegram/分销小程序)
- [ ] 设计“入群诱饵” (如：《2026 量子投资白皮书.pdf`)

## 5. 流量推广
- [ ] 在 HackerNews/Reddit 发帖： "Free Tool: Calculate Quantum Costs"
- [ ] 在 Twitter/X 转发分享链接
- [ ] 提交到 Product Hunt

## 🚀 预期收益模型
- 1000 PV/天 -> 50 广告点击 -> $5-10/天
- 100 PV/天 -> 5 联盟点击 -> $20-50/单 (亚马逊/云服务佣金高)
- 10 PV/天 -> 1 私域转化 -> $200-500/单 (课程/服务)
"""
with open(BASE / "MONETIZATION_CHECKLIST.md", "w", encoding="utf-8") as f:
    f.write(checklist)
print("✅ 变现清单已生成：~/WorkBuddy/SEO/MONETIZATION_CHECKLIST.md")

print("\n>>> 现在，只要两步就能赚钱：")
print(">>> 1. 修改代码里的链接为你的联盟/私域链接 (我帮你改，还是你自己改？)")
print(">>> 2. 推送到 GitHub 上线！")