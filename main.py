import os
from openai import OpenAI


client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


def ask_deepseek(question):

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": "你是一个简洁、耐心的编程学习助手"},
            {"role": "user", "content": question}
        ]
    )
    
    return response.choices[0].message.content


while True:

    question = input("请输入你的问题，输入q退出：")

    if question == "q":
        break

    answer = ask_deepseek(question)
    print(answer)

print("程序结束")