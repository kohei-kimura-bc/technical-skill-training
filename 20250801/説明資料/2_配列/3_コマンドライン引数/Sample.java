
public class Sample {

    public static void main(String[] args) {
        //コマンドライン引数の活用

        String x = args[1];
        System.out.println("コマンドライン引数の2つ目の要素:" + x);

        System.out.println("コマンドライン引数の要素数:" + args.length);
    }
}
