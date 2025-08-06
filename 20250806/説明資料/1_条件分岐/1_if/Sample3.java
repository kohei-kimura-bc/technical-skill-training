
public class Sample3 {

    public static void main(String[] args) {
        String color = "yellow";
        if (color == "red") {
            System.out.println("colorはred");
        } else if (color == "yellow") {
            System.out.println("colorはyellow");
        } else {
            System.out.println("colorはredでもyellowでもない");
            System.out.println("colorは" + color);
        }
    }

}
