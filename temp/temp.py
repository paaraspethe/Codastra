import openai
openai.api_key = "your API key"
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "C++ code for number is prime or not"}])
print(completion.choices[0].message.content)


