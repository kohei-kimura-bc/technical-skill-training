//練習問題１
//円の面積と体積を計算するコード
class Question1Answer{

    public static void main(String[] args){

        String shapeName = "円";            //Q1.図形の名前を保存する変数の宣言とデータの代入
        int radius = 4;                     //Q2.半径を保存する変数の宣言とデータの代入

        double area;                        //Q3.面積を保存する変数の宣言
        double volume;                      //Q4.体積を保存する変数の宣言

        final double PI = 3.14;             //Q5.円周率(定数)の宣言

        area = 2 * radius * PI;             //面積の計算
        volume = radius * radius * PI;      //体積の計算
        
        System.out.println(shapeName + "の面積と体積を求める。");
        System.out.println("面積: " + area);
        System.out.println("体積: " + volume);
    }
}