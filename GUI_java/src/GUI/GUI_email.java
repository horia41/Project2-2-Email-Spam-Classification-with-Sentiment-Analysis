package GUI;

import javafx.application.*;
import javafx.scene.Scene;
import javafx.stage.Stage;

/**
 * Main entry point. The main stage is created here. Contains some global variables<br>
 * used throughout the application. Extends the {@link Application} class.
 */
public class GUI_email extends Application {

    static Stage window;

    static final int WIDTH = 1920;

    static final int HEIGHT = 1080;



    /**
     * Sets up the Main Menu screen.
     * @param primaryStage stage  used
     */
    @Override
    public void start(Stage primaryStage) {
        window = primaryStage;
        window.setWidth(WIDTH);
        window.setHeight(HEIGHT);
        window.setFullScreen(true);

        MainMenu root = new MainMenu();

        Scene scene = new Scene(root, WIDTH, HEIGHT);

        window.setScene(scene);

        window.show();


    }

    public static void main(String[] args) {

        launch(args);

    }

}

