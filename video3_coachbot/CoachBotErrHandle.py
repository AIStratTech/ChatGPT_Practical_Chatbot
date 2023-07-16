import openai
import gradio as gr
import tiktoken
import traceback
import os


openai.api_key = os.environ["OPENAI_API_KEY"]
MAX_TOKENS = 4000


class ChatBot:
    def __init__(self, system_role):
        self.messages = [
            {"role": "system", "content": system_role},
        ]

    def count_tokens(self):
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        num_tokens = 0
        for message in self.messages:
            num_tokens += (
                4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
            )
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":  # if there's a name, the role is omitted
                    num_tokens -= 1  # role is always required and always 1 token
                num_tokens += (
                    3  # every reply is primed with <|start|>assistant<|message|>
                )
        return num_tokens

    def launch(self):
        with gr.Blocks() as demo:
            chatbot = gr.Chatbot()
            msg = gr.Textbox()
            clear = gr.ClearButton([msg, chatbot])

            def respond(input, chat_history):
                self.messages.append({"role": "user", "content": input})
                while len(self.messages) > 2 and self.count_tokens() > MAX_TOKENS:
                    self.messages = self.messages[0:1] + self.messages[2:]
                if self.count_tokens() > MAX_TOKENS:
                    self.messages = self.messages[0:1]
                    reply = "Sorry, messages are too long."
                else:
                    try:
                        chat = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo", messages=self.messages
                        )
                        reply = chat.choices[0].message["content"]
                    except openai.OpenAIError as e:
                        reply = str(e)
                        pass
                    else:
                        self.messages.append({"role": "assistant", "content": reply})
                chat_history.append((input, reply))
                return "", chat_history

            msg.submit(respond, [msg, chatbot], [msg, chatbot])
        demo.launch()


ChatBot("You are a leadership coach using the ORID framework.").launch()
