//練習問題3
class Question3Answer{
    public static void main(String[] args){
        //テストの点数を変数で宣言して、代入
        int english = 100;  //英語の点数
        int math = 70;      //数学の点数
        int japanese = 50;  //国語の点数
        
        //合格点、優秀点、満点を定数で宣言
        final int PASSING_SCORE = 60;   //Q1.合格点を定数で宣言
        final int EXCELLENT_SCORE = 90; //Q2.優秀点を定数で宣言
        final int PERFECT_SCORE = 100;  //Q3.満点を定数で宣言
        
        int totalScore = japanese + math + english;     //Q2.3教科の合計点の計算結果を代入
        double averageScore = totalScore / 3.0;         //Q2.3教科の平均点の計算結果を代入
        
        boolean isPassing = averageScore >= PASSING_SCORE;      //Q3.平均点が合格点以上なら true
        boolean isExcellent = averageScore >= EXCELLENT_SCORE;  //Q3.平均点が優秀点以上なら true
        //Q3.全教科の点数が満点(PERFECT_SCOREと等しい)なら true
        boolean isPerfect = (japanese == PERFECT_SCORE) && (math == PERFECT_SCORE) && (english == PERFECT_SCORE);
        
        //結果の表示
        System.out.println("平均点：" + averageScore + "点");
        System.out.println("合格判定：" + isPassing);
        System.out.println("優秀判定：" + isExcellent);
        System.out.println("満点判定：" + isPerfect);
        
    }
}