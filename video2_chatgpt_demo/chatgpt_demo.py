import os
import openai
import gradio as gr
import speech_recognition as sr
import requests
import json

openai.api_key = "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"
openweathermap_api_key = os.environ["WEATHER_API_KEY"]

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant that provides weather information.",
    },
]


def get_weather(city_name: str):
    # 定義 OpenWeatherMap API 的請求參數
    weather_params = {
        "q": city_name,
        "appid": openweathermap_api_key,
        "units": "metric",
    }
    # 使用 OpenWeatherMap API 獲取指定地點的天氣資訊
    weather_response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather", params=weather_params
    )
    weather_data = json.loads(weather_response.text)
    return weather_data


# 從openwather API取得天氣資訊
def get_weather_data(function_call):
    if function_call:
        arguments = function_call.get("arguments")
        arguments = json.loads(arguments)
        function_response = get_weather(
            city_name=arguments.get("city_name"),
        )
        function_response = json.dumps(function_response)
        return function_response
    return None


# 將天氣資訊文本進行解析、處理和生成可用的文本報告
def compose_weather_summary(user_input, function_response):
    second_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "user", "content": user_input},
            {
                "role": "function",
                "name": "get_weather",
                "content": function_response,
            },
        ],
    )
    return second_response.choices[0].message.content


# 利用chatgpt的function_call取得地名, 就是實體辨識
def find_place_names(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=[
            {
                "name": "get_weather",
                "description": "get current weather",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city_name": {
                            "type": "string",
                            "description": "city_name",
                        },
                    },
                    "required": ["city_name"],
                },
            }
        ],
        function_call="auto",
    )
    reply = response["choices"][0]["message"]
    function_call = reply.get("function_call")
    return function_call


# 將中文的語音轉成中文
def speech_to_text(audio_file):
    r = sr.Recognizer()  # 預設辨識英文
    with sr.WavFile(audio_file) as source:  # 讀取wav檔
        audio = r.record(source)
    try:
        return r.recognize_google(audio, language="zh-TW")
    except LookupError:
        print("Could not understand audio")
        return None


def chat(audio_file):
    user_input = speech_to_text(audio_file)
    if user_input:
        user_location = find_place_names(user_input)
        weather_data = get_weather_data(user_location)
        if weather_data:
            gpt_summary = compose_weather_summary(user_input, weather_data)
    return user_input, gpt_summary


inputs = gr.inputs.Textbox(label="User input")
outputs = gr.outputs.Textbox(label="Response")

demo = gr.Interface(
    fn=chat,
    inputs=gr.Audio(source="microphone", type="filepath"),
    outputs=["text", "text"],
    title="ChatGPT Demo",
)
demo.launch(share=True)
