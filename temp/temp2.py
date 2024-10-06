from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained CodeGPT model and tokenizer
model_name = "EleutherAI/gpt-neo-codex"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# User input prompt for code generation
prompt = "Write a Python function to calculate the factorial of a number."

# Tokenize input prompt
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# Generate code based on input prompt
output = model.generate(input_ids, max_length=200, num_return_sequences=1, no_repeat_ngram_size=2)

# Decode and print the generated code
generated_code = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_code)
