class Human:  # クラスの宣言（先頭は大文字にする    

    # インスタンスの初期化（コンストラクタ）
    def __init__(self, name, age, height, address):
        self.name = name
        self.age = age
        self.height = height
        self.address = address
        pass

    # インスタンスメソッド
    def say_hello(self):
        print(f"私の名前は{self.name}で、{self.age}歳です。\n身長は{self.height}cmで、{self.address}に住んでいます。 ")


kimura = Human("Kimura", 18, 180, "Tokyo")
suzuki = Human("Suzuki", 16, 170, "Osaka")

kimura.say_hello()
suzuki.say_hello()
