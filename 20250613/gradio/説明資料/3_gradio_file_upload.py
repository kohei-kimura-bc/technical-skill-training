import gradio as gr


# ファイル内容を読み込んで表示する関数
def display_file_content(file):
    try:
        with open(file.name, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"


# Gradio Blocksを使用してUIを構築
with gr.Blocks() as demo:
    # Markdownで説明を表示
    gr.Markdown(
        "## ファイルアップロードアプリ\n以下にファイルをアップロードしてください。アップロードしたファイルの内容を表示します。"
    )

    # ファイルアップロードコンポーネント
    file_input = gr.File(label="ファイルを選択")
    file_output = gr.Textbox(label="ファイル内容")
    submit_button = gr.Button("表示")

    # ボタンが押されたときに内容を表示する処理を設定
    submit_button.click(display_file_content, inputs=file_input, outputs=file_output)

# アプリを起動
demo.launch()
