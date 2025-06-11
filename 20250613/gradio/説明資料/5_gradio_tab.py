import gradio as gr


# ファイル内容を読み込んで表示する関数
def display_file_content(file):
    try:
        with open(file.name, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"


# 四則演算を行う関数
def arithmetic_operations(a, b, operation):
    try:
        a, b = float(a), float(b)
        if operation == "加算":
            return a + b
        elif operation == "減算":
            return a - b
        elif operation == "乗算":
            return a * b
        elif operation == "除算":
            return a / b if b != 0 else "ゼロで割ることはできません"
        else:
            return "不正な操作です"
    except ValueError:
        return "数値を入力してください"


# 挨拶を返す関数
def greeting(name):
    return f"こんにちは、{name}さん！"


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
