# -*- coding: utf-8 -*-
"""Tokenizers.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18reS-TmZqQB-BOaXS6OoGxPJZqd0YNNr
"""

from google.colab import userdata
from huggingface_hub import login
from transformers import AutoTokenizer

hf_token = userdata.get('HF_TOKEN')
login(hf_token, add_to_git_credential=True)

tokenizer = AutoTokenizer.from_pretrained('meta-llama/Meta-Llama-3.1-8B', trust_remote_code=True)

text = "I am excited to show Tokenizers in action to my LLM engineers"
tokens = tokenizer.encode(text)
tokens

len(tokens)

tokenizer.decode(tokens)

tokenizer.batch_decode(tokens)

tokenizer.vocab

tokenizer = AutoTokenizer.from_pretrained('meta-llama/Meta-Llama-3.1-8B-Instruct', trust_remote_code=True)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell a funny joke about monkeys and cheese."},
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
prompt

PHI3_MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
QWEN2_MODEL_NAME = "Qwen/Qwen2-7B-Instruct"
STARCODER2_MODEL_NAME = "bigcode/starcoder2-3b"

phi3_tokenizer = AutoTokenizer.from_pretrained(PHI3_MODEL_NAME, trust_remote_code=True)

text = "I am excited to show tokenizers in action."
print(phi3_tokenizer.encode(text))

print(tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True))
print()
print(phi3_tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True))

qwen2_tokenizer = AutoTokenizer.from_pretrained(QWEN2_MODEL_NAME, trust_remote_code=True)
print(tokenizer.encode(text))
print()
print(phi3_tokenizer.encode(text))
print()
print(qwen2_tokenizer.encode(text))

starcoder_tokenizer = AutoTokenizer.from_pretrained(STARCODER2_MODEL_NAME, trust_remote_code=True)
code = """
def add(a, b):
    return a + b
"""

tokens = tokenizer.encode(code)
print(tokenizer.batch_decode(tokens))

tokens_phi3 = phi3_tokenizer.encode(code)
print(phi3_tokenizer.batch_decode(tokens_phi3))

tokens_qwen2 = qwen2_tokenizer.encode(code)
print(qwen2_tokenizer.batch_decode(tokens_qwen2))

tokens_starcoder = starcoder_tokenizer.encode(code)
print(starcoder_tokenizer.batch_decode(tokens_starcoder))

