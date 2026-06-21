from llm_client import ask_deepseek


while True:

    question = input("请输入你的问题，输入q退出：")

    if question == "q":
        break

    answer = ask_deepseek(question)
    print(answer)

    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write("用户：" + question + "\n")
        f.write("模型：" + answer + "\n")
        f.write("------\n")

print("程序结束")