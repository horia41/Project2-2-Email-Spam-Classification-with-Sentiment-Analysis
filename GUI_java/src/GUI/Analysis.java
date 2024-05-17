package GUI;

import javafx.scene.control.Button;
import javafx.scene.control.ScrollPane;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Background;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;


public class Analysis extends Pane {

    static final int WIDTH = 1920;
    static final int HEIGHT = 1080;

    static final double MAX_TEXT_WIDTH = WIDTH - 100;
    Analysis(String textInput, String result) {
        setBackground(Background.fill((Color.web("#CCCCCC"))));

        //Logo Image
        ImageView Logo = new ImageView("file:GUI_java/src/GUI/resources/BackGround2.2.png");
        Logo.setRotate(-90);
        Logo.setX(WIDTH - 350);
        Logo.setY(HEIGHT - 200);
        Logo.setPreserveRatio(true);
        Logo.setFitWidth(300);

        //Home and Exit Button
        Button homeButton = new Button();
        homeButton.setLayoutX(WIDTH - 250);
        homeButton.setLayoutY(35);
        ImageView homeImage = new ImageView("file:GUI_java/src/GUI/resources/home22.png");
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
        ImageView exitImage = new ImageView("file:GUI_java/src/GUI/resources/cross22.png");
        exitImage.setPreserveRatio(true);
        exitImage.setFitHeight(80);
        exit.setGraphic(exitImage);
        exit.setStyle("-fx-border-color: transparent;" +
                "-fx-background-color: transparent;");


        Text text = new Text("This is the input text");
        text.setLayoutX(50);
        text.setLayoutY(200);
        text.setStyle("-fx-font-size: 24px; " +
                "-fx-font-family: Calibri; " +
                "-fx-text-fill: white;");

        Text printText = new Text(textInput);
        printText.setLayoutX(50);
        printText.setLayoutY(250);
        printText.setStyle("-fx-font-size: 24px; " +
                "-fx-font-family: Calibri; " +
                "-fx-text-fill: white;");
        printText.maxWidth(MAX_TEXT_WIDTH);

        ScrollPane scrollPane = new ScrollPane();
        scrollPane.setContent(printText);
        scrollPane.setFitToWidth(true);
        scrollPane.setFitToHeight(true);
        scrollPane.setLayoutX(50);
        scrollPane.setLayoutY(300);
        scrollPane.setPrefSize(WIDTH - 100, HEIGHT - 500);

        Text textR = new Text("This is the result");
        textR.setLayoutX(50);
        textR.setLayoutY(50);
        textR.setStyle("-fx-font-size: 24px; " +
                "-fx-font-family: Calibri; " +
                "-fx-text-fill: white;");

        Text printText_result = new Text(result);
        printText_result.setLayoutX(50);
        printText_result.setLayoutY(100);
        printText_result.setStyle("-fx-font-size: 24px; " +
                "-fx-font-family: Calibri; " +
                "-fx-text-fill: white;");
        getChildren().addAll(scrollPane, printText_result, textR, exit, text, printText, Logo, homeButton);

    }
}


