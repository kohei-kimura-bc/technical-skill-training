"""
以下のGradioを実装しているプログラムの関数部分をモジュール化してください
"""

import gradio as gr
from my_module import display_file_content, arithmetic_operations, greeting


# Gradio Blocksを使用してUIを構築
with gr.Blocks() as demo:
    with gr.Tabs():
        # タブ1: ファイルアップロード
        with gr.Tab("ファイルアップロード"):
            gr.Markdown(
                "## ファイルアップロードアプリ\n以下にファイルをアップロードしてください。アップロードしたファイルの内容を表示します。"
            )
            file_input = gr.File(label="ファイルを選択")
            file_output = gr.Textbox(label="ファイル内容")
            submit_button = gr.Button("表示")
            submit_button.click(
                display_file_content, inputs=file_input, outputs=file_output
            )

        # タブ2: 四則演算
        with gr.Tab("四則演算"):
            gr.Markdown("## 四則演算\n2つの数値を入力し、操作を選択してください。")
            num1 = gr.Textbox(label="数値1")
            num2 = gr.Textbox(label="数値2")
            operation = gr.Dropdown(
                ["加算", "減算", "乗算", "除算"], label="操作を選択"
            )
            result = gr.Textbox(label="結果")
            calculate_button = gr.Button("計算")
            calculate_button.click(
                arithmetic_operations, inputs=[num1, num2, operation], outputs=result
            )

        # タブ3: 挨拶
        with gr.Tab("挨拶"):
            gr.Markdown("## 挨拶アプリ\n名前を入力してください。")
            name_input = gr.Textbox(label="名前")
            greeting_output = gr.Textbox(label="挨拶")
            greeting_button = gr.Button("挨拶する")
            greeting_button.click(greeting, inputs=name_input, outputs=greeting_output)

# アプリを起動
demo.launch()
