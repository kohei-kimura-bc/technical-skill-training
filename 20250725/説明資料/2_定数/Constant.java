/*
10行目のコメントアウトを解除するとコンパイルエラーが起きる
*/

public class Constant{
    public static void main(String[] args) {
        final int MAX_SCORE = 100;
        //MAX_SCORE = 200;  //定数は変更できない
        System.out.println("このテストは"+ MAX_SCORE + "点満点だ。");
    }
}