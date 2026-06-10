#!/usr/bin/env python3
"""
SEO 流量工厂 - 一键部署上线
功能：将 docs/ 内容推送到 GitHub，触发 Vercel 自动部署
"""
import os, subprocess, datetime
from pathlib import Path

BASE = Path.home() / "WorkBuddy" / "SEO"
REPO_URL = "https://github.com/your-username/seo-factory.git"  # 替换为你的仓库
DOCS = BASE / "docs"
REMOTE_NAME = "origin"

def run(cmd):
    print(f">>> {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ 错误：{result.stderr}")
        return False
    if result.stdout:
        print(result.stdout.strip())
    return True

def main():
    print(f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 🔥 SEO 流量工厂 · 一键部署启动")
    
    # 1. 检查 docs/ 内容
    articles = list(DOCS.glob("*.html"))
    if not articles:
        print("❌ docs/ 目录为空，先生成内容！")
        return False
    print(f"✅ 检测到 {len(articles)} 篇文章待部署")
    
    # 2. 进入仓库目录
    os.chdir(BASE)
    
    # 3. 添加所有修改
    if not run("git add -A"): return False
    
    # 4. 检查是否有变更
    status = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    if not status.stdout.strip():
        print("ℹ️  无新变更，跳过部署")
        return True
    
    # 5. 提交
    msg = f"🚀 Auto Deploy: {len(articles)} articles [{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}] v4.5"
    if not run(f'git commit -m "{msg}"'): return False
    
    # 6. 推送
    if not run(f"git push {REMOTE_NAME} main"):
        print("❌ 推送失败，请检查：")
        print("   1. 仓库地址是否正确")
        print("   2. GitHub Token 是否过期 (请运行: git remote set-url origin <新 token URL>")
        return False
    
    print(f"\n✅ 部署成功！等待 Vercel 构建...")
    print(f"🌐 访问：https://your-domain.vercel.app")  # 替换为你的域名
    return True

if __name__ == "__main__":
    main()