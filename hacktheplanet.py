import json
import torch
import time
import threading
import openai  # Import the OpenAI package
from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, Y, RIGHT, END
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
from llama_cpp import Llama

# Llama Model
llm = Llama(model_path="D:\\ggml-vicuna-7b-4bit\\ggml-vicuna-7b-4bit-rev1.bin")

def llama_generate(prompt, max_tokens=200):
    output = llm(prompt, max_tokens=max_tokens)
    return output['choices'][0]['text']

# GPT-Neo Model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = GPTNeoForCausalLM.from_pretrained('EleutherAI/gpt-neo-125m').to(device)
tokenizer = GPT2Tokenizer.from_pretrained('EleutherAI/gpt-neo-125m')

tokenizer.add_special_tokens({'pad_token': '[PAD]'})
model.config.pad_token_id = tokenizer.pad_token_id

def gpt3_generate(model, tokenizer, chunk, max_length=2000, time_limit=50.0):
    start_time = time.time()

    inputs = tokenizer.encode(chunk, return_tensors='pt', truncation=True, max_length=512).to(device)
    attention_mask = inputs.ne(tokenizer.pad_token_id).float().to(device)
    outputs = model.generate(inputs, max_length=max_length, do_sample=True, max_time=time_limit, attention_mask=attention_mask)

    response = tokenizer.decode(outputs[0])
    end_time = time.time()

    return response, end_time - start_time


  
def gpt4_generate(prompt, max_tokens=200):
    # Make sure to replace "YOUR_API_KEY" with your actual API key
    api_key = "apikeyhere"
    openai.api_key = api_key
    
    # Make a request to the GPT-4 API using the v1/chat/completions endpoint
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Replace "gpt-4" with the appropriate engine name for GPT-4
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )
    
    # Extract the generated text from the response
    generated_text = response["choices"][0]["message"]["content"]
    return generated_text

# Define a function to facilitate intercommunication between the models
def intercommunication(prompt):
    # Generate response using Llama
    llama_response = llama_generate(prompt)
    
    # Generate response using GPT-Neo
    gpt_neo_response, _ = gpt3_generate(model, tokenizer, prompt)
    
    # Generate response using GPT-4 (ChatGPT plugin model)
    gpt4_response = gpt4_generate(prompt)
    
    # Combine the responses
    response = f"Llama: {llama_response}\nGPT-Neo: {gpt_neo_response}\nChatGPT: {gpt4_response}\n"
    
    return response

# GUI setup
root = Tk()
root.title("AI Conversation")
root.geometry("800x600")

Label(root, text="Enter input:").grid(row=0, column=0, sticky="W")

input_text = Entry(root, width=100)
input_text.grid(row=1, column=0)

output_text = Text(root, wrap="word", width=80, height=20)
output_text.grid(row=2, column=0, padx=10, pady=10, rowspan=6)

scrollbar = Scrollbar(root, command=output_text.yview)
scrollbar.grid(row=2, column=1, sticky="ns", rowspan=6)
output_text.config(yscrollcommand=scrollbar.set)
# Generate response and update GUI
def on_generate_click():
    user_input = input_text.get()
    response = intercommunication(user_input)
    output_text.insert(END, f"You: {user_input}\n{response}\n")
    input_text.delete(0, END)  # Clear input field

# Bind enter key to button click event
def on_enter_key(event):
    on_generate_click()

Button(root, text="Generate", command=on_generate_click).grid(row=1, column=1)
root.bind('<Return>', on_enter_key)

root.mainloop()
