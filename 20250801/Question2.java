// ===============================
// 問題2: 配列の合計を求める
// int型の配列 numbers に格納された数値の合計を求め、変数 total に代入してください。
// ===============================

public class Question2 {

    public static void main(String[] args) {
        int[] numbers = {3, 7, 2, 9, 5};
        int total = 0;

        // ここにコードを記述してください
        for(int i = 0; i < numbers.length; i++){
            total += numbers[i];
        }
        
        System.out.println("合計: " + total); // 出力例: 合計: 26
    }
}
