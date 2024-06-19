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
        Button start = new Button();
        ImageView startImage = new ImageView("file:GUI_java/src/GUI/resources/start22.png");
        startImage.setPreserveRatio(true);
        startImage.setFitWidth(300.0);
        start.setGraphic(startImage);
        start.setStyle("-fx-border-color: transparent;-fx-background-color: transparent;");
        start.setLayoutX(810.0);
        start.setLayoutY(680.0);
        start.setOnAction((event) -> {
            GUI_email.window.getScene().setRoot(new TextInput());
        });
        Button exit = new Button();
        exit.setLayoutX(1770.0);
        exit.setLayoutY(50.0);
        exit.setOnAction((e) -> {
            System.exit(0);
        });
        ImageView exitImage = new ImageView("file:GUI_java/src/GUI/resources/cross22.png");
        exitImage.setPreserveRatio(true);
        exitImage.setFitHeight(150.0);
        exit.setGraphic(exitImage);
        exit.setStyle("-fx-border-color: transparent;-fx-background-color: black;");
        ImageView Logo = new ImageView("file:GUI_java/src/GUI/resources/BackGround2.2.png");
        Logo.setRotate(-90.0);
        Logo.setX(310.0);
        Logo.setY(-200.0);
        Logo.setPreserveRatio(true);
        Logo.setFitWidth(1300.0);
        this.getChildren().addAll(new Node[]{start, exit, Logo});
    }
}
