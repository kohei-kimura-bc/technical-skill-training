class Student:  # クラスの宣言（先頭は大文字にする）
    # クラス変数(クラスに共通の変数を定義する)
    school = "hoge大学"

    # インスタンスの初期化（コンストラクタ）
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    # インスタンスメソッド
    def say_hello(self):
        print(f"My name is {self.name}. I am {self.age} years old.")


kimura = Student("Kimura", 18)
suzuki = Student("Suzuki", 16)

kimura.say_hello()
suzuki.say_hello()
