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
        ],
        stream=True
    )

    answer = ""

    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="")
            answer += content

    print()
    
    return answer
