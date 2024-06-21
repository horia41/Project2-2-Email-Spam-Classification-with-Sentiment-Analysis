package GUI;

import javafx.scene.Node;
import javafx.scene.control.Button;
import javafx.scene.control.ScrollPane;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Background;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;

public class Info extends Pane {
    static final int WIDTH = 1920;
    static final int HEIGHT = 1080;

    Info() {
        this.setBackground(Background.fill(Color.web("#000000")));
        // Home Button
        Button homeButton = new Button();
        homeButton.setLayoutX(1670.0);
        homeButton.setLayoutY(35.0);
        ImageView homeImage = new ImageView("file:GUI_java/src/GUI/resources/home22.png");
        homeImage.setPreserveRatio(true);
        homeImage.setFitHeight(140.0);
        homeButton.setGraphic(homeImage);
        homeButton.setStyle("-fx-border-color: transparent;-fx-background-color: transparent;");
        homeButton.setOnAction((event) -> {
            GUI_email.window.getScene().setRoot(new MainMenu());
        });

        // Exit Button
        Button exit = new Button("x");
        exit.setLayoutX(1720.0);
        exit.setLayoutY(4.0);
        exit.setOnAction((e) -> {
            System.exit(0);
        });
        exit.setStyle("-fx-font-size: 94px; -fx-font-family: Calibri; -fx-text-fill: white; -fx-background-color: black; -fx-border-color: transparent;");



        Text text = new Text();
        text.setWrappingWidth(1700); // Slightly less than the ScrollPane width
        text.setStyle("-fx-font-size: 69px; -fx-font-family: Calibri; -fx-text-fill: white;");
        // TODO: Add the text to be displayed here
        text.setText("This program is designed to analyze text data. The user can input text data and the program will analyze the text data and provide the user with the results. The user can then view the results and analyze the data further. The program is designed to be user-friendly and easy to use. The user can input text data in the text area and click the analyze button to analyze the data. The program will then display the results in the results area. The user can then view the results and analyze the data further. The program is designed to be user-friendly and easy to use. The user can input text data in the text area and click the analyze button to analyze the data. The program will then display the results in the results area. The user can then view the results and analyze the data further. The program is designed to be user-friendly and easy to use. The user can input text data in the text area and click the analyze button to analyze the data. The program will then display the results in the results area. The user can then view the results and analyze the data further.");
        text.setFill(Color.WHITE);

        ScrollPane scrollPane = new ScrollPane();
        scrollPane.setContent(text);
        scrollPane.setFitToWidth(true);
        scrollPane.setFitToHeight(true);
        scrollPane.setPrefSize(1920, 1080); // Set a preferred size for the ScrollPane
        scrollPane.setLayoutX(100.0);
        scrollPane.setLayoutY(200.0); // Adjusted Y position
        scrollPane.setStyle("-fx-background: transparent; -fx-background-color: transparent;");

        this.getChildren().addAll(new Node[]{scrollPane, exit, homeButton});
    }
}
/**
 * // Create TextFlow to hold different styled texts
 *         TextFlow textFlow = new TextFlow();
 *         textFlow.setLayoutX(100.0);
 *         textFlow.setLayoutY(100.0);
 *
 *         // Split the text into parts and style them individually
 *         String[] parts = {
 *             "This ", "program", " is designed to analyze text data. The user can input text data and the ", "program",
 *             " will analyze the text data and provide the user with the results. The user can then view the results and analyze the data further. The ",
 *             "program", " is designed to be user-friendly and easy to use. The user can input text data in the text area and click the ",
 *             "analyze", " button to analyze the data. The ", "program",
 *             " will then display the results in the results area. The user can then view the results and analyze the data further. The ",
 *             "program", " is designed to be user-friendly and easy to use. The user can input text data in the text area and click the ",
 *             "analyze", " button to analyze the data. The ", "program",
 *             " will then display the results in the results area. The user can then view the results and analyze the data further. The ",
 *             "program", " is designed to be user-friendly and easy to use. The user can input text data in the text area and click the ",
 *             "analyze", " button to analyze the data. The ", "program",
 *             " will then display the results in the results area. The user can then view the results and analyze the data further."
 *         };
 *
 *         for (String part : parts) {
 *             Text text = new Text(part);
 *             text.setFont(Font.font("Calibri", 30));
 *             text.setFill(Color.WHITE);
 *             if (part.equals("program") || part.equals("analyze")) {
 *                 text.setStyle("-fx-font-weight: bold;");
 *             }
 *             textFlow.getChildren().add(text);
 *         }
 *
 *         ScrollPane scrollPane = new ScrollPane();
 *         scrollPane.setContent(textFlow);
 *         scrollPane.setFitToWidth(true);
 *         scrollPane.setFitToHeight(true);
 *         scrollPane.setPrefSize(1920, 1080); // Set a preferred size for the ScrollPane
 *         scrollPane.setLayoutX(100.0);
 *         scrollPane.setLayoutY(100.0); // Adjusted Y position
 *         scrollPane.setStyle("-fx-background: transparent; -fx-background-color: transparent;");
 *
 *         root.getChildren().add(scrollPane);
 */