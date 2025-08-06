/*
問題5：
以下のコードでは、配列アクセスとゼロ除算の両方が含まれています。try-catchを使ってどちらの例外も捕捉し、それぞれに応じたエラーメッセージを表示してください。
 */

public class Question5 {

    public static void main(String[] args) {
        int[] data = {10, 20, 30};
        int index = 5;
        int divisor = 0;

        try {
            int value = data[index]; // 配列アクセス
            int result = value / divisor; // ゼロ除算
            System.out.println("結果: " + result);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("エラー：配列の範囲外アクセスです。");
        } catch (ArithmeticException e) {
            System.out.println("エラー：ゼロ除算が発生しました。");
        }
    }
}
