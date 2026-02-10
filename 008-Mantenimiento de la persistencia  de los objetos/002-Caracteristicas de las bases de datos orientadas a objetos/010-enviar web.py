import json
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:3b-instruct"

# Read HTML file
with open("guardado.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Build prompt using file contents
prompt = f"""
Analyze the following HTML file and answer the question.

QUESTION:
How many houses are in this file?

HTML CONTENT:
{html_content}
"""

data = {
    "model": MODEL,
    "prompt": prompt,
    "stream": False
}

req = urllib.request.Request(
    OLLAMA_URL,
    data=json.dumps(data).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

with urllib.request.urlopen(req) as response:
    result = json.loads(response.read().decode("utf-8"))
    print(result["response"])
          
