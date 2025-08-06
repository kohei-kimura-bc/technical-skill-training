/*
問題7：
以下のコードでは、nullの文字列に対してlength()を呼び出して例外が発生します。try-catchを使って例外を処理し、エラーメッセージを表示してください。
 */

public class Question7 {

    public static void main(String[] args) {
        String text = null;
        System.out.println("文字数: " + text.length());
    }
}
