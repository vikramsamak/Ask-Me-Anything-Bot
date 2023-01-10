import openai
openai.api_key = "YOUR-OPENAI'S-API-KEY"

print("---ASK ME ANYTHING BOT ---")

while True:
    question = input("Ask me anything:-")

    response = openai.Completion.create(
        model="text-davinci-003", prompt=question, temperature=0, max_tokens=100)
    res = (response["choices"][0]["text"])
    res = res.replace("\n", "")
    print("ASK ME ANYTHING Bot:-", res)
