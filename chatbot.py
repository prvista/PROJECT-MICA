# import openai

# # Set up your OpenAI API key
# openai.api_key = 'sk-proj-y8pwEJ5x40n4yMsjKIV3T3BlbkFJ60hFLua6HsTmyiO5gCLx'

# def chat_with_gpt(prompt):
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         max_tokens=150
#     )
#     return response.choices[0].text.strip()

# print("Welcome to ChatGPT! Let's chat. Type 'exit' to end the conversation.")

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'exit':
#         print("ChatGPT: Goodbye!")
#         break
#     else:
#         response = chat_with_gpt(user_input)
#         print("ChatGPT:", response)
