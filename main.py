import os
from openai import OpenAI


client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
while True:

    question = input("请输入你的问题，输入q退出：")

    if question == "q":
        break

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": "你是一个简洁、耐心的编程学习助手"},
            {"role": "user", "content": question}
        ]
    )

    print(response.choices[0].message.content)

    print("\n本次调用 token 用量")
    print("输入 token：", response.usage.prompt_tokens)
    print("输出 token：", response.usage.completion_tokens)
    print("总计 token：", response.usage.total_tokens)