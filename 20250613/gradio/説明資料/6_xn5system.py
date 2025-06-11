# 実行コマンド：python -m uvicorn main:app --host 0.0.0.0
# ローカルホスト：http://127.0.0.1:8000

import gradio as gr

# from fastapi import FastAPI
# from modules.common.create_history_table import (
#     create_analyze_history,
#     create_first_triage_history,
#     create_second_triage_history,
# )
# from modules.common.log_setting import output_log
# from modules.screen1.process_msg_files import process_msg_files
# from modules.screen2.process_xlsx_files import process_xlsx_files
# from modules.screen3.download_first_triage import download_first_triage
# from modules.screen3.process_second_triage import process_second_triage
# from modules.screen4.download_ticket_list import download_ticket_list
# from modules.screen4.process_tickets import process_tickets


with gr.Blocks(
    css="footer {visibility: hidden}",
    title="Vulnerability Management Automation for Auto-ISAC",
) as demo:
    with gr.Tabs():
        with gr.TabItem("レポートメール解析"):
            gr.Markdown("## ファイルアップロード")
            upload_files_1 = gr.Files(file_types=[".msg"], file_count="multiple")
            execute_button_1 = gr.Button("実行")
            gr.Markdown("## 解析レポート一覧")
            file_table = gr.DataFrame(
                headers=[
                    "#",
                    "レポートメール",
                    "受信日時",
                    "処理",
                    "ステータス",
                    "メッセージ",
                ],
                interactive=False,
            )
            gr.Markdown("## ファイルダウンロード")
            download_files = gr.Files()
            execute_button_1.click(
                # fn=process_msg_files,
                inputs=upload_files_1,
                outputs=[file_table, download_files],
            )
            gr.Markdown("## 解析履歴")
            history_button1 = gr.Button("解析履歴表示")
            analyze_history = gr.Markdown("")
            history_button1.click(inputs=None, outputs=analyze_history)
            with gr.Column():
                analyze_history
        with gr.TabItem("1次トリアージ結果アップロード"):
            gr.Markdown("## 1次トリアージ結果アップロード")
            upload_files_2 = gr.Files(file_types=[".xlsx"], file_count="multiple")
            execute_button_2 = gr.Button("実行")
            gr.Markdown("## ステータス")
            file_table = gr.DataFrame(
                headers=["#", "ファイル名", "処理", "ステータス", "メッセージ"],
                interactive=False,
            )
            execute_button_2.click(inputs=upload_files_2, outputs=file_table)
            gr.Markdown("## 1次トリアージ結果アップロード履歴")
            history_button2 = gr.Button("アップロード履歴表示")
            first_triage_history = gr.HTML("")
            history_button2.click(
                # fn=create_first_triage_history,
                inputs=None,
                outputs=first_triage_history,
            )
            with gr.Column():
                first_triage_history
        with gr.TabItem("2次トリアージ"):
            gr.Markdown("## 2次トリアージ入力用ファイルダウンロード")
            download_button = gr.Button("2次トリアージ入力用ファイルダウンロード")
            download_files = gr.Files(interactive=False)
            download_button.click(inputs=None, outputs=download_files)
            gr.Markdown("## 2次トリアージ結果アップロード")
            upload_files_3 = gr.Files(file_types=[".xlsx"], file_count="multiple")
            execute_button_3 = gr.Button("実行")
            gr.Markdown("## アップロードファイル一覧")
            file_table = gr.DataFrame(
                headers=["#", "ファイル名", "処理", "ステータス", "メッセージ"],
                interactive=False,
            )
            execute_button_3.click(inputs=upload_files_3, outputs=file_table)
            gr.Markdown("## 2次トリアージ結果アップロード履歴")
            history_button3 = gr.Button("アップロード履歴表示")
            second_triage_history = gr.HTML("")
            history_button3.click(
                # fn=create_second_triage_history,
                inputs=None,
                outputs=second_triage_history,
            )
            with gr.Column():
                second_triage_history
        with gr.TabItem(
            "Jiraチケット更新"
        ):  # INQのダウンロード、更新は旧業務フローのため無効化
            gr.Markdown("## チケットダウンロード")
            # inq_checkbox = gr.Checkbox(label='INQ', value=True)
            aut_checkbox = gr.Checkbox(label="AUT", value=True)
            subtask_checkbox = gr.Checkbox(label="サブタスク", value=True)
            download_button = gr.Button("ダウンロード")
            download_files = gr.Files(interactive=False)
            download_button.click(
                # fn=download_ticket_list,
                # inputs=[inq_checkbox, aut_checkbox, subtask_checkbox],
                inputs=[aut_checkbox, subtask_checkbox],
                outputs=download_files,
            )
            gr.Markdown("## チケットアップロード")
            upload_files_4 = gr.Files(file_types=[".xlsx"], file_count="multiple")
            execute_button_4 = gr.Button("実行")
            gr.Markdown("## アップロードファイル一覧")
            file_table = gr.DataFrame(
                headers=["#", "ファイル名", "処理", "ステータス", "メッセージ"],
                interactive=False,
            )
            execute_button_4.click(inputs=upload_files_4, outputs=file_table)
demo.launch()
