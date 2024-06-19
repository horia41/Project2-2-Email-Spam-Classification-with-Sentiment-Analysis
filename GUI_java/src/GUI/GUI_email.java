package GUI;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class GUI_email extends Application {

    public static Stage window;

    @Override
    public void start(Stage primaryStage) {
        window = primaryStage;

        // Initial scene
        MainMenu mainMenu = new MainMenu();

        window.setTitle("Email Analysis");
        window = primaryStage;
        window.setWidth(1920.0);
        window.setHeight(1080.0);
        window.setFullScreen(true);
        MainMenu root = new MainMenu();
        Scene scene = new Scene(root, 1920.0, 1080.0);
        window.setScene(scene);
        window.show();
    }

    public static void main(String[] args) {

        launch(args);

    }
}


