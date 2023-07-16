import os
import openai
import gradio as gr

openai.api_key = os.environ["OPENAI_API_KEY"]

messages = [
    {
        "role": "system",
        "content": "You are a leadership coach using the ORID framework.",
    },
]


def chat(user_input):
    if user_input:
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply


inputs = gr.inputs.Textbox(label="User input")
outputs = gr.outputs.Textbox(label="Response")

gr.Interface(
    fn=chat,
    inputs=inputs,
    outputs=outputs,
    title="CoachBot Basic",
).launch(share=True)
