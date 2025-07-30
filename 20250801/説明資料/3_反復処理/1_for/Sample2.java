
public class Sample2 {

    public static void main(String[] args) {
        // 飲み物の名前を配列に格納
        String[] drinks = {
            "コーヒー",
            "紅茶",
            "オレンジジュース",
            "リンゴジュース",
            "ミルク",
            "コーラ",
            "レモネード",
            "緑茶",
            "炭酸水",
            "スポーツドリンク"
        };

        // 配列の要素を順番に表示
        for (int i = 0; i < drinks.length; i++) {
            System.out.println("飲み物: " + drinks[i]);
        }
    }
}
