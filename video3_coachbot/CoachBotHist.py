import openai
import gradio as gr
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

messages = [
    {
        "role": "system",
        "content": "You are a leadership coach using the ORID framework.\
            Instructions: Only answer questions related to leadership. \
            Answer the question as truthfully as possible, and if you're unsure of the answer, say \"Sorry, I don't know\"",
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
