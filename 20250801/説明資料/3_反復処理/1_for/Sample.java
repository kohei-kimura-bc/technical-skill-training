
public class Sample {

    public static void main(String[] args) {

        //for文開始
        System.out.println("▼for文開始");
        // 1から5までの数字を繰り返す
        for (int i = 1; i <= 5; i++) {
            System.out.println("  ▼" + i + "回目の繰り返し処理開始");
            System.out.println("  数字: " + i);
            System.out.println("  ▲" + i + "回目の繰り返し処理終了");
        }
        //for文終了
        System.out.println("▲for文終了");
    }
}
