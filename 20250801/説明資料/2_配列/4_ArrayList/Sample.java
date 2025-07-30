import java.util.ArrayList;
import java.util.Collections;

public class Sample {
    public static void main(String[] args) {
        // ① ArrayListの作成（文字列型）
        ArrayList<String> fruits = new ArrayList<>();

        // ② 要素の追加（add）
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");

        System.out.println("初期リスト: " + fruits); // [Apple, Banana, Cherry]

        // ③ 要素の挿入（index指定のadd）
        fruits.add(1, "Orange");
        System.out.println("挿入後: " + fruits); // [Apple, Orange, Banana, Cherry]

        // ④ 要素の取得（get）
        String firstFruit = fruits.get(0);
        System.out.println("最初のフルーツ: " + firstFruit); // Apple

        // ⑤ 要素の変更（set）
        fruits.set(2, "Mango");
        System.out.println("変更後: " + fruits); // [Apple, Orange, Mango, Cherry]

        // ⑥ 要素の削除（remove）
        fruits.remove("Orange");   // オブジェクトで削除
        fruits.remove(0);          // インデックスで削除
        System.out.println("削除後: " + fruits); // [Mango, Cherry]

        // ⑦ 要素の検索（contains, indexOf）
        boolean hasBanana = fruits.contains("Banana");
        int cherryIndex = fruits.indexOf("Cherry");
        System.out.println("バナナはあるか？ " + hasBanana);       // false
        System.out.println("チェリーの位置: " + cherryIndex);      // 1

        // ⑧ 要素数の取得（size）
        System.out.println("リストのサイズ: " + fruits.size()); // 2

        // ⑨ ループ処理
        System.out.println("全要素を表示:");
        for (String fruit : fruits) {
            System.out.println("- " + fruit);
        }

        // ⑩ ソート（Collections.sort）
        fruits.add("Grape");
        fruits.add("Peach");
        Collections.sort(fruits);
        System.out.println("ソート後: " + fruits); // アルファベット順に並ぶ

        // ⑪ すべて削除（clear）
        fruits.clear();
        System.out.println("クリア後のリスト: " + fruits); // []
    }
}
