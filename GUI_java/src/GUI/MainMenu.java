package GUI;

import javafx.scene.Node;
import javafx.scene.control.Button;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Background;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;

public class MainMenu extends Pane {
    static final int WIDTH = 1920;
    static final int HEIGHT = 1080;

    MainMenu() {
        this.setBackground(Background.fill(Color.web("#000000")));

        Button start = new Button("Start");
        start.setStyle("-fx-font-size: 60px; -fx-font-family: 'Calibri Light'; -fx-text-fill: white; -fx-background-color: black; -fx-border-color: white;");
        start.setLayoutX(850.0);
        start.setLayoutY(575.0);
        start.setOnAction((event) -> {
            GUI_email.window.getScene().setRoot(new TextInput());
        });

        Button exit = new Button("x");
        exit.setLayoutX(1760.0);
        exit.setLayoutY(-15);
        exit.setOnAction((e) -> {
            System.exit(0);
        });
        exit.setStyle("-fx-font-size: 94px; -fx-font-family: Calibri; -fx-text-fill: white; -fx-background-color: black; -fx-border-color: transparent;");

        ImageView background = new ImageView("file:GUI_java/src/GUI/resources/homeScreen.png");
        background.setX(0);
        background.setPreserveRatio(true);
        background.setFitWidth(1920.0);

        Button info = new Button();
        info.setLayoutX(30);
        info.setLayoutY(30);
        ImageView homeImage = new ImageView("file:GUI_java/src/GUI/resources/info.jpg");
        homeImage.setPreserveRatio(true);
        homeImage.setFitHeight(80);
        info.setGraphic(homeImage);
        info.setStyle("-fx-border-color: transparent;-fx-background-color: transparent;");
        info.setOnAction((event) -> {
            GUI_email.window.getScene().setRoot(new Info());
        });

        this.getChildren().addAll(new Node[]{background, info, start, exit});
    }
}
