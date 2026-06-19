from llm_client import ask_deepseek


while True:

    question = input("请输入你的问题，输入q退出：")

    if question == "q":
        break

    answer = ask_deepseek(question)
    print(answer)

print("程序结束")