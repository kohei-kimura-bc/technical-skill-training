/*
問題3：
以下のコードは、配列のインデックスを範囲外でアクセスして例外が発生します。try-catchで例外を処理し、「不正なインデックスです」と表示してください。
 */

public class Question3 {

    public static void main(String[] args) {
        int[] nums = {10, 20, 30};
        try {
            System.out.println("値: " + nums[5]);   //例外が発生しうる処理
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("不正なインデックスです");
        }
    }
}
