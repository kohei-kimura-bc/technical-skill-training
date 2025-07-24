//練習問題2
class Question2Answer{
    public static void main(String[] args){
        //変数の宣言
        int num1 = 2, num2 = 3;
        int sum,dif,pro;

        sum = num1 + num2;  //Q1.足し算
        dif = num1 - num2;  //Q2.引き算
        pro = num1 * num2;  //Q3.掛け算
        
        System.out.println("和: " + sum + ", 差: " + dif + ", 積: " + pro);     //Q2.結果を表示

        sum += 2;     //Q3.複合代入演算子を用いて 2 を足す
        
        //Q4.結合演算子を用いて、文字列型変数 result に文字列と数値型変数 sum を代入 
        String result = "和にさらに2を足した値は" + sum;     
        System.out.println(result);     //Q4の結果を表示
    }
}