import os
from openai import OpenAI


client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "user", "content": "请用一句话解释什么是 API"}
    ]
)

print(response.choices[0].message.content)