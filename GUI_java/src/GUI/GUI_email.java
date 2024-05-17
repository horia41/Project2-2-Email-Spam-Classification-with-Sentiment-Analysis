package GUI;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.stage.Screen;

public class GUI_email extends Application {

    public static Stage window;

    @Override
    public void start(Stage primaryStage) {
        window = primaryStage;

        // Initial scene
        MainMenu mainMenu = new MainMenu();
        Scene scene = new Scene(mainMenu, Screen.getPrimary().getBounds().getWidth(), Screen.getPrimary().getBounds().getHeight());

        window.setTitle("Email Analysis");
        window.setScene(scene);
        window.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
