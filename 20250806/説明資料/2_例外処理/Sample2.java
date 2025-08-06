//=========================
// 1つ目のコマンドライン引数で除算を行うプログラム
// 
// 例外処理有りのパターン
//=========================


public class Sample2 {

    public static void main(String[] args) {
        try {
            int result = 100 / Integer.parseInt(args[0]); // 例外が発生する可能性のある行
            System.out.println(result);
        }catch(ArrayIndexOutOfBoundsException e){
            System.out.println("エラー：引数を入力してください。");
        } 
        catch (ArithmeticException e) {
            System.out.println("エラー：0で割ることはできません。");
        } catch (NumberFormatException e) {
            System.out.println("エラー：数字以外を入力することはできません。");
        } finally {
            System.out.println("この行は必ず実行されます。");
        }
    }
}
