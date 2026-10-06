from openai import OpenAI

client = OpenAI()

print("🤖 Tamil Personal Assistant started!")
print("Type 'exit' to stop.\n")

while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("Assistant: Goodbye! 👋")
        break

    response = client.responses.create(
        model="gpt-5-mini",
        input=[
            {
                "role": "system",
                "content": (
                    "You are my personal assistant. "
                    "Understand Tamil, Tanglish, and English. "
                    "Reply in the same language the user uses. "
                    "Keep responses simple and helpful."
                ),
            },
            {
                "role": "user",
                "content": user_message,
            },
        ],
    )

    print("Assistant:", response.output_text)