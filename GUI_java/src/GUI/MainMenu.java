package GUI;

import javafx.scene.control.Button;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Background;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.stage.Screen;

public class MainMenu extends BorderPane {

    private final double WIDTH;
    private final double HEIGHT;

    private static final Color BACKGROUND_COLOR = Color.web("#000000");

    public MainMenu() {
        // Get screen dimensions
        WIDTH = Screen.getPrimary().getBounds().getWidth();
        HEIGHT = Screen.getPrimary().getBounds().getHeight();

        setBackground(Background.fill(BACKGROUND_COLOR));

        // Start Button
        Button startButton = new Button();
        ImageView startImage = new ImageView("file:GUI_java/src/GUI/resources/start22.png");
        startImage.setPreserveRatio(true);
        startImage.setFitWidth(300);
        startButton.setGraphic(startImage);
        startButton.setStyle("-fx-border-color: transparent;" + "-fx-background-color: transparent;");
        startButton.setOnAction(event -> GUI_email.window.getScene().setRoot(new TextInput()));

        // Center the Start Button
        setCenter(startButton);
    }
}
