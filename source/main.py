import json
import cloudscraper
import matplotlib.pyplot as plt
import pandas as pd
import mplcyberpunk

# 创建一个 cloudscraper 实例
scraper = cloudscraper.create_scraper()

response = scraper.get("https://greasyfork.org/zh-CN/scripts/473912/stats.json")

# 检查状态
response.raise_for_status()
print(response.json())

star_json = json.loads(response.text)

star_date = []
star_installs = []
star_temp = 0

for i in star_json:
    star_date.append(str(i))
    star_temp += star_json[i]['installs']
    star_installs.append(star_temp)

print(star_date)
print(star_installs)

plt.style.use("cyberpunk")
plt.figure(figsize=(20, 10), dpi=100)
plt.rcParams['font.sans-serif'] = ['HYWenHei'] # 用来正常显示中文标签SimHei
plt.title("Github搜索净化", fontdict={'size': 30})
plt.xlabel("时间", fontdict={'size': 30})
plt.ylabel("总安装数（Greasy Fork）", fontdict={'size': 30})
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.plot(pd.to_datetime(star_date), star_installs, linewidth=4.0)
plt.savefig('history.png')
