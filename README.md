# HyperGPT
All in AI MODELS 

# How To Use:
```
hyper = HyperGPT()
hyper.base_api = "https://api.biswax.dev/{}"

prompt = "what is your name?"
```
# chatgpt response
```
print("ChatGPT Response: ")
chatgpt = hyper.chatbot(prompt, model="gpt")
print(chatgpt.response)
```
# facebook's llama response
```
print("\nLLAMA Response: ")
llama = hyper.chatbot(prompt, model="llama")
print(llama.response)
```

# Generate Image
```
print("\nGenerate Image: ")
imageai = hyper.generate_image("elon musk", model="3d")
print("Image is ready: ", imageai.result)
```
