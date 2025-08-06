//============================
// BMIを計算するプログラム
//
// コマンドライン引数で身長(cm)、体重(kg)を入力する
// 例) java Sample3 150 40
//
// 以下の場合に応じて、独自のエラーを出力する
// ①身長が100未満の場合
// ②身長が230より大きい場合
// ③体重が20未満の場合
//============================


// ①身長が100未満の例外
class HeightTooSmallException extends Exception {
    public HeightTooSmallException(String message) {
        super(message);
    }
}

// ②身長が230より大きい場合の例外
class HeightTooLargeException extends Exception {
    public HeightTooLargeException(String message) {
        super(message);
    }
}

// ③体重が20未満の例外
class WeightTooSmallException extends Exception {
    public WeightTooSmallException(String message) {
        super(message);
    }
}

public class Sample3 {
    public static void main(String[] args) {
        int height = Integer.parseInt(args[0]);
        int weight = Integer.parseInt(args[1]);

        try {
            if (height < 100) {
                throw new HeightTooSmallException("身長が100cm未満です");           // ①の例外処理へ
            }
            if (height > 230) {
                throw new HeightTooLargeException("身長が230cmより大きいです");     // ②の例外処理へ
            }
            if (weight < 20) {
                throw new WeightTooSmallException("体重が20kg未満です");            // ③の例外処理へ
            }

            double bmi = weight / Math.pow(height / 100.0, 2);
            System.out.println("BMI: " + bmi);

        } catch (HeightTooSmallException e) {
            System.out.println("身長エラー1: " + e.getMessage());    // ①の例外発生時の処理
        } catch (HeightTooLargeException e) {
            System.out.println("身長エラー2: " + e.getMessage());    // ②の例外発生時の処理
        } catch (WeightTooSmallException e) {
            System.out.println("体重エラー: " + e.getMessage());    // ③の例外発生時の処理
        }
    }
}