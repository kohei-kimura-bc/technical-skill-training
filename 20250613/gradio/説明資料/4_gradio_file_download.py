import gradio as gr


# テキストファイルを生成する関数
def create_text_file(input_text):
    # 入力された文字列をファイルに書き込む
    file_path = "output.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(input_text)
    return file_path


# Gradio Blocksを使用してUIを構築
with gr.Blocks() as demo:
    # Markdownで説明を表示
    gr.Markdown(
        "## テキストファイル生成アプリ\n以下に文字列を入力してください。入力された内容に基づいてテキストファイルを生成します。"
    )

    # テキストボックスでユーザーからの入力を受け取る
    text_input = gr.Textbox(
        label="文字列を入力", placeholder="ここに文字列を入力してください"
    )

    # ファイルダウンロード用のボタン
    submit_button = gr.Button("ファイルを生成")

    # ファイルダウンロード用のコンポーネント
    file_output = gr.File(label="生成されたファイル")

    # ボタンが押されたときにファイルを生成する処理を設定
    submit_button.click(create_text_file, inputs=text_input, outputs=file_output)

# アプリを起動
demo.launch()
