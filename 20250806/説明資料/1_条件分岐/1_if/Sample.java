
public class Sample {

    public static void main(String[] args) {

        // コマンドライン引数で受け取ったString型の数字をInteger.parseInt()でint型にキャスト
        int customerAge = Integer.parseInt(args[0]);

        if (customerAge < 20) {
            System.out.println("未成年にはお酒は売ることができません。");
        }
    }
}
