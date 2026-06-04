import os, json, datetime, urllib.request, subprocess

os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7897'
BASE = os.path.expanduser('~/WorkBuddy/SEO')
os.makedirs(f'{BASE}/articles', exist_ok=True)
os.makedirs(f'{BASE}/docs', exist_ok=True)

print('🚀 启动 SEO...')
topics = [{'title': 'AI自动化工具2026'}, {'title': 'Python部署指南'}, {'title': 'Web3安全'}]
try:
    req = urllib.request.Request('https://www.reddit.com/r/technology/hot.json?limit=3', headers={'User-Agent': 'Mozilla/5.0'})
    data = json.load(urllib.request.urlopen(req, timeout=10))
    real = [{'title': x['data']['title']} for x in data['data']['children'] if x['data']['score']>50][:3]
    if real: topics = real; print('✅ Reddit OK')
except: print('⚠️ Fallback')

