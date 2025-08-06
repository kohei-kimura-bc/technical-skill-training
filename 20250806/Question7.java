/*
問題7：
以下のコードでは、nullの文字列に対してlength()を呼び出して例外が発生します。try-catchを使って例外を処理し、エラーメッセージを表示してください。
 */

public class Question7 {

    public static void main(String[] args) {
        String text = null;
        try {
            System.out.println("文字数: " + text.length()); //例外が発生しうる処理
        } catch (NullPointerException e) {
            System.out.println("null文字列でlength()は呼び出せません");
        }
    }
}
