/*
10行目をコメントアウトして、11行目のコメントアウトを解除するとコンパイルエラーが起きる
*/


class Variable{
    public static void main(String[] args){
        String name;    // 文字型変数 name の宣言
        name = "山田";  // 変数 name に文字列を代入
        int age = 25;   // 数値型変数 age を宣言して数値データを代入
        //age = 25;     // 型を指定しないと、エラーになる

        // メッセージの表示
        String message = name + "さんは" + age +"歳です。";
        System.out.println(message);

    }
}