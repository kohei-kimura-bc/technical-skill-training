
public class Sample {

    public static void main(String[] args) {
        String str = "apple,orange,melon";
        System.out.println("str: " + str);

        String[] fruits = str.split(",");
        System.out.println(fruits[0]);
        System.out.println(fruits[1]);
        System.out.println(fruits[2]);
    }
}
