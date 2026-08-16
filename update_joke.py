import json
import math
from datetime import datetime

JOKES_PER_DAY = 10

# Load jokes
with open("jokes.json", "r", encoding="utf-8") as f:
    jokes = json.load(f)

total_jokes = len(jokes)
cycle_days  = math.ceil(total_jokes / JOKES_PER_DAY)

# Pilih grup berdasarkan hari dalam siklus
day_of_year = datetime.now().timetuple().tm_yday
day_index   = (day_of_year - 1) % cycle_days
start       = day_index * JOKES_PER_DAY

today_jokes = jokes[start : start + JOKES_PER_DAY]

# Build baris tabel
rows = "\n".join(
    f"| {j['q']} | {j['a']} |"
    for j in today_jokes
)

joke_block = f"""<!-- JOKE_START -->
> *Jokes ala bapak-bapak Indonesia, gratis tidak dipungut biaya 🧔*
> *(Siklus hari ke-{day_index + 1}/{cycle_days} — jokes {start + 1}–{start + JOKES_PER_DAY} dari {total_jokes})*

| 🎤 Pertanyaan | 😆 Jawaban |
|:---|:---|
{rows}
<!-- JOKE_END -->"""

# Update README
import re
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

pattern     = r"<!-- JOKE_START -->.*?<!-- JOKE_END -->"
new_content = re.sub(pattern, joke_block, content, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"✅ Hari ke-{day_index + 1}/{cycle_days} — Jokes {start + 1}–{start + JOKES_PER_DAY}/{total_jokes}")
for j in today_jokes:
    print(f"  ❓ {j['q']}")
    print(f"  😄 {j['a']}")
