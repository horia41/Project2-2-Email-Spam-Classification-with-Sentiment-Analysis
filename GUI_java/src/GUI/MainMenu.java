package GUI;

import javafx.scene.control.Button;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Background;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;


public class MainMenu extends Pane {

    static final int WIDTH = 1920;
    static final int HEIGHT = 1080;

    MainMenu() {
        //Set background color to black
        setBackground(Background.fill((Color.web("#000000"))));

        Button start = new Button();
        ImageView startImage = new ImageView("file:GUI_java/src/GUI/resources/start22.png"); //path from repository root
        startImage.setPreserveRatio(true);
        startImage.setFitWidth(300);
        start.setGraphic(startImage);
        start.setStyle("-fx-border-color: transparent;" +
                "-fx-background-color: transparent;");
        start.setLayoutX((WIDTH - 300) / 2);
        start.setLayoutY(HEIGHT - 400);
        start.setOnAction(event -> {
            GUI_email.

                    window.getScene().setRoot(new TextInput());
        });


        Button exit = new Button();
        exit.setLayoutX(WIDTH - 150);
        exit.setLayoutY(50);
        exit.setOnAction(e -> System.exit(0));
        ImageView exitImage = new ImageView("file:GUI_java/src/GUI/resources/cross22.png");//path from repository root
        exitImage.setPreserveRatio(true);
        exitImage.setFitHeight(150);
        exit.setGraphic(exitImage);
        exit.setStyle("-fx-border-color: transparent;"+
                "-fx-background-color: black;");

        ImageView Logo = new ImageView("file:GUI_java/src/GUI/resources/BackGround2.2.png"); //path from repository root
        Logo.setRotate(-90);
        Logo.setX(1920/2 - 650);
        Logo.setY(-200);
        Logo.setPreserveRatio(true);
        Logo.setFitWidth(1300);

        getChildren().addAll(start, exit, Logo);
    }
}
