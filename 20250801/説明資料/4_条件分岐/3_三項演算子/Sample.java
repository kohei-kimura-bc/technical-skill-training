
public class Sample {

    public static void main(String[] args) {
        int score = 75;
        String result;

        // 三項演算子を使って合格・不合格を判定
        result = (score >= 60) ? "合格" : "不合格";

        System.out.println("点数: " + score);
        System.out.println("結果: " + result);
    }
}
