import gradio as gr


def greet(name):
    return f"Hello, {name}さん!"


# インターフェースを作成
demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch()
