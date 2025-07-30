
public class Sample {

    public static void main(String[] args) {
        int i = 1; // カウンタ変数の初期化

        // do-while文開始
        System.out.println("▼do-while文開始");
        do {
            System.out.println("  ▼" + i + "回目の繰り返し処理開始");
            System.out.println("  数字: " + i);
            System.out.println("  ▲" + i + "回目の繰り返し処理終了");
            i++; // カウントアップ
        } while (i <= 5);
        // do-while文終了
        System.out.println("▲do-while文終了");
    }
}
