import openai

# Set your OpenAI API key
openai.api_key = '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'

# Define a function to ask a question
def ask_question(question, chat_log=None):
    if chat_log is None:
        chat_log = []
    prompt = f'{"".join(chat_log)}Human: {question}\nAI:'
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150
    )
    answer = response.choices[0].text.strip()
    chat_log.append(f'Human: {question}\nAI: {answer}\n')
    return answer, chat_log

# Start a conversation
chat_log = []
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response, chat_log = ask_question(user_input, chat_log)
    print("ChatGPT:", response)
