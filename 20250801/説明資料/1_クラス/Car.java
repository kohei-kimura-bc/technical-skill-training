//クラス、インスタンス、フィールド、メソッド
class Car{
    private String carName;         //車種名のフィールド
    private int maximumCapacity;    //最大積載人数のフィールド
    //コンストラクタ
    Car(String carName, int maximumCapacity){
            this.carName = carName;
            this.maximumCapacity = maximumCapacity;
        }
    //getterメソッド
    public String getCarName(){
        return carName;
    }
    public int getMaximumCapacity(){
        return maximumCapacity;
    }
    //setterメソッド
    public void setCarName(String carName){
        this.carName = carName;
    }
    public void setMaximumCapacity(int maximumCapacity){
        this.maximumCapacity = maximumCapacity;
    }
    //runメソッド
    void run(){     
        System.out.println(getMaximumCapacity() + "人乗りの" + getCarName() + "が走ります。");
    }
    //メインメソッド
    public static void main(String[] args){     
        Car car1 = new Car("セレナ",8);     //car1インスタンスの生成
        Car car2 = new Car("ノート",5);     //car2インスタンスの生成
        //runメソッドの呼び出し
        car1.run();     //car1インスタンスから呼び出し
        car2.run();     //car2インスタンスから呼び出し
        /*
        //setterメソッドを呼び出してデータの変更
        car1.setCarName("ルークス");
        car1.setMaximumCapacity(4);
        System.out.println("--------------------");
        //再びrunメソッドの呼び出し
        car1.run();
        car2.run();
        */
    }
}