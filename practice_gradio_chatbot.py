



import gradio as gr
import random
from openai import OpenAI
# adding code for running local lm via lM studio

#client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

client = OpenAI(
   
    api_key = "your-api",
)

def chat_logic(message,chat_history):
    messages = []
    for msg_pair in chat_history:
        messages.append({"role":"user","content":msg_pair[0]})
        messages.append({"role":"assistant","content":msg_pair[1]})
    #link question of user and answer of bot.
    messages.append({"role":"user","content":message})
    #print(messages)
    # running by local lm studio

#     chat_completion = client.chat.completions.create(
#         model="your llm model if you want to run it locally",
#         messages=messages,
#         stream=True
# )
    chat_history.append([message,"loading..."])

    chat_completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=messages,
      stream=True)
    chat_history.append([message,"loading..."])

    yield "", chat_history

    chat_history[-1][1]= ""
    for chunk in chat_completion:
       delta = chunk.choices[0].delta.content or ""
       chat_history[-1][1] += delta
       yield "", chat_history

    return "",chat_history




with gr.Blocks() as demo:
  gr.Markdown("# CHAT BOT WITH CHATGPT")
  message = gr.Textbox(label="input message")
  chatbot = gr.Chatbot(label="Superduper chatbot")
  message.submit(chat_logic,[message,chatbot],[message,chatbot])

demo.launch(debug=True)
#gr.Error("custom message")

