//練習問題3
class Question3{
    public static void main(String[] args){
        //テストの点数を変数で宣言して、代入
        int english = 100;  //英語の点数
        int math = 70;      //数学の点数
        int japanese = 50;  //国語の点数
        
        //合格点、優秀点、満点を定数で宣言
        //Q1.ここに、合格点 PASSING_SCORE を 60 として定数で宣言
        //Q2.ここに、優秀点 EXCELLENT_SCORE を 90 として定数で宣言
        //Q3.ここに、満点 PERFECT_SCORE を 100 として定数で宣言
        
        int totalScore = ________________;      //Q2.3教科の合計点の計算結果を代入
        int averageScore = ________________;    //Q2.3教科の平均点の計算結果を代入
        
        boolean isPassing = ___________________;              //Q3.平均点が合格点以上なら true
        boolean isExcellent = ______________________;         //Q3.平均点が優秀点以上なら true
        //Q3.全教科の点数が満点(PERFECT_SCOREと等しい)なら true
        boolean isPerfect = _______________________________________;
        
        //計算結果・評価の表示
        System.out.println("平均点：" + averageScore + "点");
        System.out.println("合格判定：" + isPassing);
        System.out.println("優秀判定：" + isExcellent);
        System.out.println("満点判定：" + isPerfect);
        
    }
}