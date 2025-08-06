/*
問題4：
ユーザーが入力した文字列を整数に変換しようとしています。数値でない文字列を入力したときに発生する例外を処理し、「数値を入力してください」と表示するようにしてください。
 */

import java.util.Scanner;

public class Question4 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("年齢を入力してください: ");
        String input = scanner.nextLine();

        int age = Integer.parseInt(input);
        System.out.println("あなたの年齢: " + age);
    }
}
