import json
import os
from datetime import datetime

# Load jokes
with open("jokes.json", "r", encoding="utf-8") as f:
    jokes = json.load(f)

# Pick joke based on day of year so it changes every day
day_of_year = datetime.now().timetuple().tm_yday
joke = jokes[day_of_year % len(jokes)]

# Build the joke block
joke_block = f"""<!-- JOKE_START -->
> *Jokes ala bapak-bapak Indonesia, gratis tidak dipungut biaya 🧔*

| 🎤 Pertanyaan | 😆 Jawaban |
|:---|:---|
| {joke['q']} | {joke['a']} |
<!-- JOKE_END -->"""

# Update README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

import re
pattern = r"<!-- JOKE_START -->.*?<!-- JOKE_END -->"
new_content = re.sub(pattern, joke_block, content, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"✅ Updated joke #{day_of_year % len(jokes) + 1}/{len(jokes)}: {joke['q']}")
