// ===============================
// 問題1: 人間クラスの定義
// Q1 ~ Q5 に解答してください
// ===============================

public class Question1 {

    // フィールドをprivateで宣言（カプセル化）
    private String name;//Q1.ここに名前のフィールドを宣言
    private int age;//Q1.ここに年齢のフィールドを宣言

    // コンストラクタ
    //Q2.ここにコンストラクタを作成
    Question1(String name, int age){
        this.name = name;
        this.age = age;
    }

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
        Question1 human1 = new Question1("たろう",20);//Q3.ここにhuman1インスタンス生成
        Question1 human2 = new Question1("はなこ",18);//Q3.ここにhuman2インスタンス生成

        // walkメソッドの呼び出し
        human1.walk();//Q4.ここでhuman1インスタンスで、walkメソッドの呼び出し
        human2.walk();//Q4.ここでhuman2インスタンスで、walkメソッドの呼び出し

        // setterメソッドでデータの変更
        human1.setName("じろう");//Q5.ここでhuman1インスタンスの name のデータを変更
        human1.setAge(15);//Q5.ここでhuman1インスタンスの age のデータを変更
        System.out.println("--------------------");
        // 再びwalkメソッドの呼び出し
        human1.walk();
        human2.walk();
        
    }
}