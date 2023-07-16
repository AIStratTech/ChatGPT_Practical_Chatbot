import openai
import gradio as gr
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

messages = [
    {
        "role": "system",
        "content": "You are a leadership coach using the ORID framework.",
    },
]


with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(input, chat_history):
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message["content"]
        messages.append({"role": "assistant", "content": reply})
        chat_history.append((input, reply))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
demo.launch(share=True)
