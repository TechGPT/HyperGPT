# HyperGPT
All in one AI MODELS

# How To Use:
```
hyper = HyperGPT()
hyper.base_api = "https://api.biswax.dev/{}"

prompt = "what is your name?"
```
## chatgpt response
```
chatgpt = hyper.chatbot(prompt, model="gpt")
print(chatgpt.response)
```
## facebook's llama response
```
llama = hyper.chatbot(prompt, model="llama")
print(llama.response)
```

## Generate Image
```
imageai = hyper.generate_image("elon musk", model="3d")
print("Image is ready: ", imageai.result)
```
