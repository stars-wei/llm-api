import os
from openai import OpenAI


client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

question = input("请输入你的问题：")

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "user", "content": question}
    ]
)

print(response.choices[0].message.content)