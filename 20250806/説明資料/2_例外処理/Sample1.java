//=========================
// 1つ目のコマンドライン引数で除算を行うプログラム
// 
// 例外処理なしのパターン
//=========================

public class Sample1 {

    public static void main(String[] args) {
            int result = 100 / Integer.parseInt(args[0]); // 例外が発生する可能性のある行
            System.out.println(result);
    }
}
