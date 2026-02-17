import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAIAPI")
)

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain the three-body problem in simple terms."}
    ],
    temperature=0.3
)

print(response.choices[0].message.content)

