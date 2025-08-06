/*
問題3：
以下のコードは、配列のインデックスを範囲外でアクセスして例外が発生します。try-catchで例外を処理し、「不正なインデックスです」と表示してください。
 */

public class Question3 {

    public static void main(String[] args) {
        int[] nums = {10, 20, 30};
        System.out.println("値: " + nums[5]);
    }
}
