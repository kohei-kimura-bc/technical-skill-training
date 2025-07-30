
public class Sample {

    public static void main(String[] args) {
        int i = 1; // カウンタ変数の初期化

        // while文開始
        System.out.println("▼while文開始");
        while (i <= 5) {
            System.out.println("  ▼" + i + "回目の繰り返し処理開始");
            System.out.println("  数字: " + i);
            System.out.println("  ▲" + i + "回目の繰り返し処理終了");
            i++; // カウントアップ
        }
        // while文終了
        System.out.println("▲while文終了");
    }
}
