// ===============================
// 問題3: 配列の逆順出力
// String型の配列 names に格納された要素を逆順に出力してください。
// ===============================

public class Question3 {

    public static void main(String[] args) {
        String[] names = {"Taro", "Hanako", "Jiro", "Yuki"};

        // ここにコードを記述してください
        for(int i = names.length-1; i >= 0; i--){
            System.out.println(names[i]);
        }
    }
}
