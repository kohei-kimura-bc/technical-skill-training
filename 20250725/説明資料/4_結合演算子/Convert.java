/*
結合演算子「+」を用いて、String型変数にint型変数のデータを結合して代入できる
*/
class Convert{
    public static void main(String[] args){
        String drink = "コーラ";    //文字型変数 drink に "コーラ" を代入
        int price = 200;            //数値型変数 price に 200 を代入
        String result;              //文字型変数 result を宣言

        result = drink + "の値段は" + price + "円でした。";     //文字型変数 result にint型変数 price のデータを結合して代入 
        System.out.println(result);     //文字列として表示される
    }
}