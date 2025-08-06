import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;
import java.util.logging.Level;
import java.util.logging.Handler;

public class LoggingExample {
    public static void main(String[] args) {
        try {
            // Loggerの取得（名前は任意）
            Logger logger = Logger.getLogger("MyLogger");
            
            // FileHandlerを作成し、ログをファイルに出力
            FileHandler fh = new FileHandler("app.log");
            
            // SimpleFormatterを設定して、出力フォーマットをシンプルに
            SimpleFormatter formatter = new SimpleFormatter();
            fh.setFormatter(formatter);
            
            // Loggerにハンドラを追加
            logger.addHandler(fh);
            
            // ログレベルを設定（重要度の閾値）
            logger.setLevel(Level.INFO);
            
            // ログ出力
            logger.info("これは情報レベルのログです。");
            logger.warning("これは警告レベルのログです。");
            logger.severe("これは重大なエラーのログです。");
            
            // ハンドラを閉じる
            fh.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}