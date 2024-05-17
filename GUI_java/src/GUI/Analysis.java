package GUI;

import javafx.scene.control.Button;
import javafx.scene.control.ScrollPane;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Background;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;
import javafx.stage.Screen;

public class Analysis extends BorderPane {

    private final double WIDTH;
    private final double HEIGHT;

    private static final double MAX_TEXT_WIDTH = Screen.getPrimary().getBounds().getWidth() - 100;

    public Analysis(String textInput, String result) {
        // Get screen dimensions
        WIDTH = Screen.getPrimary().getBounds().getWidth();
        HEIGHT = Screen.getPrimary().getBounds().getHeight();

        setBackground(Background.fill(Color.web("#CCCCCC")));

        // Logo Image
        ImageView logo = new ImageView("file:GUI_java/src/GUI/resources/BackGround2.2.png");
        logo.setRotate(-90);
        logo.setPreserveRatio(true);
        logo.setFitWidth(300);

        // Home Button
        Button homeButton = new Button();
        ImageView homeImage = new ImageView("file:GUI_java/src/GUI/resources/home22.png");
        homeImage.setPreserveRatio(true);
        homeImage.setFitHeight(40);
        homeButton.setGraphic(homeImage);
        homeButton.setStyle("-fx-border-color: transparent;" + "-fx-background-color: transparent;");
        homeButton.setOnAction(event -> GUI_email.window.getScene().setRoot(new MainMenu()));

        // Text Display
        Text resultText = new Text(result);
        resultText.setWrappingWidth(MAX_TEXT_WIDTH);
        ScrollPane scrollPane = new ScrollPane(resultText);
        scrollPane.setFitToWidth(true);
        scrollPane.setFitToHeight(true);

        // Bottom panel with home button
        setTop(homeButton);
        setCenter(scrollPane);
        setRight(logo);
    }
}
