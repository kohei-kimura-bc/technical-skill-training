"""
体重と身長を入力するとBMIを計算してくれるアプリをgradioで作成してください

＜条件＞
- 体重と身長を入力し、「計算」ボタンを押すとBMIが計算され、画面に表示される
- 入力値が不正な場合、エラーポップアップが表示される

"""

import gradio as gr


# 数値入力を検証する関数
def get_number(value, min_value, unit):
    try:
        num = int(value)
        if num < min_value:
            raise AssertionError(f"{min_value}{unit}以上の値を入力してください")
        return num, None  # 正常時は数値を返し、エラーはNone
    except ValueError:
        return None, "入力された値は数字ではありません"  # エラーメッセージを返す
    except AssertionError as e:
        return None, str(e)  # エラーメッセージを返す


# BMIを計算する関数
def calculate_bmi(weight, height):
    # 入力値の検証
    valid_weight, weight_error = get_number(weight, 30, "kg")
    valid_height, height_error = get_number(height, 100, "cm")

    if weight_error:  # 体重にエラーがある場合
        return None, weight_error
    if height_error:  # 身長にエラーがある場合
        return None, height_error

    # BMI計算
    bmi = valid_weight / (valid_height / 100) ** 2
    return round(bmi, 2), None  # 正常時はBMIを返し、エラーはNone


# Gradio Blocksを使用してUIを構築
with gr.Blocks() as demo:
    gr.Markdown("## BMI計算アプリ")
    gr.Markdown("体重と身長を入力して、BMIを計算しましょう！")

    with gr.Row():
        weight_input = gr.Number(label="体重 (kg)")
        height_input = gr.Number(label="身長 (cm)")

    calculate_button = gr.Button("計算")
    bmi_output = gr.Textbox(label="BMI結果")

    # ボタンがクリックされたときにBMIを計算
    def on_calculate(weight, height):
        bmi, error = calculate_bmi(weight, height)
        if error:  # エラーがある場合はエラーメッセージを表示
            raise gr.Error(error)
        else:
            return bmi

    calculate_button.click(
        fn=on_calculate,
        inputs=[weight_input, height_input],
        outputs=[bmi_output],
    )

# アプリケーションの実行
demo.launch()
