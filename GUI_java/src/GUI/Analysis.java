package GUI;

import javafx.scene.control.Button;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Background;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;


public class Analysis extends Pane {

    static final int WIDTH = 1920;
    static final int HEIGHT = 1080;

    Analysis(String textInput, String result) {
        setBackground(Background.fill((Color.web("#CCCC00"))));

        //Logo Image
        ImageView Logo = new ImageView("file:GUI/resources/BackGround2.2.png");
        Logo.setRotate(-90);
        Logo.setX(WIDTH - 350);
        Logo.setY(HEIGHT - 200);
        Logo.setPreserveRatio(true);
        Logo.setFitWidth(300);

        //Home and Exit Button
        Button homeButton = new Button();
        homeButton.setLayoutX(WIDTH - 250);
        homeButton.setLayoutY(35);
        ImageView homeImage = new ImageView("file:GUI/resources/home22.png");
        homeImage.setPreserveRatio(true);
        homeImage.setFitHeight(140);
        homeButton.setGraphic(homeImage);
        homeButton.setStyle("-fx-border-color: transparent;" +
                "-fx-background-color: transparent;");
        homeButton.setOnAction(event -> {
            GUI_email.window.getScene().setRoot(new MainMenu());
        });

        Button exit = new Button();
        exit.setLayoutX(WIDTH - 150);
        exit.setLayoutY(50);
        exit.setOnAction(e -> System.exit(0));
        ImageView exitImage = new ImageView("file:GUI/resources/cross22.png");
        exitImage.setPreserveRatio(true);
        exitImage.setFitHeight(80);
        exit.setGraphic(exitImage);
        exit.setStyle("-fx-border-color: transparent;" +
                "-fx-background-color: transparent;");


        Text text = new Text("This is the analysis page");
        text.setLayoutX(50);
        text.setLayoutY(50);
        text.setStyle("-fx-font-size: 24px; " +
                "-fx-font-family: Calibri; " +
                "-fx-text-fill: white;");

        Text printText = new Text(textInput);
        printText.setLayoutX(50);
        printText.setLayoutY(100);
        printText.setStyle("-fx-font-size: 24px; " +
                "-fx-font-family: Calibri; " +
                "-fx-text-fill: white;");
        getChildren().addAll(homeButton, exit, text, printText, Logo);

    }
}


