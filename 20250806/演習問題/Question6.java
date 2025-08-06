/*
問題6：
次のコードは、ユーザーが入力した2つの整数の割り算を行います。除数が0のときに例外が発生するので、try-catchで適切に処理してください。
 */

import java.util.Scanner;

public class Question6 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("割られる数を入力してください: ");
        int a = scanner.nextInt();
        System.out.print("割る数を入力してください: ");
        int b = scanner.nextInt();
        int result = a / b;
        System.out.println("結果: " + result);
    }
}
