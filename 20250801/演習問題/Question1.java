// ===============================
// 問題1: 人間クラスの定義
// Q1 ~ Q5 に解答してください
// ===============================

public class Question1 {

    // フィールドをprivateで宣言（カプセル化）
    //Q1.ここに名前のフィールドを宣言
    //Q1.ここに年齢のフィールドを宣言

    // コンストラクタ
    //Q2.ここにコンストラクタを作成

    // getterメソッド
    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    // setterメソッド
    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    // walkメソッド
    void walk() {
        System.out.println(getAge() + "歳の" + getName() + "さんが歩きます。");
    }

    public static void main(String[] args) {
        //Q3.ここにhuman1インスタンス生成
        //Q3.ここにhuman2インスタンス生成

        // walkメソッドの呼び出し
        //Q4.ここでhuman1インスタンスで、walkメソッドの呼び出し
        //Q4.ここでhuman2インスタンスで、walkメソッドの呼び出し

        // setterメソッドでデータの変更
        //Q5.ここでhuman1インスタンスの name のデータを変更
        //Q5.ここでhuman1インスタンスの age のデータを変更
        System.out.println("--------------------");
        // 再びwalkメソッドの呼び出し
        human1.walk();
        human2.walk();
        
    }
}