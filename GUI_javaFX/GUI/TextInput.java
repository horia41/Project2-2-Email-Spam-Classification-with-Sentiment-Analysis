package GUI;

import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.ScrollPane;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Background;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.stage.FileChooser;
import java.io.File;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;


public class TextInput extends Pane {

    static final int WIDTH = 1920;
    static final int HEIGHT = 1080;

    static final Color BACKGROUND_COLOR = Color.web("#000000");


    TextInput() {
        setBackground(Background.fill(BACKGROUND_COLOR));
        //Logo Image
        ImageView Logo = new ImageView("file:GUI/resources/BackGround2.2.png");
        Logo.setRotate(-90);
        Logo.setX(WIDTH - 350);
        Logo.setY(HEIGHT - 200);
        Logo.setPreserveRatio(true);
        Logo.setFitWidth(300);

        // Text Area
        TextArea textArea = new TextArea();
        textArea.setPromptText("Enter your text here");
        textArea.setMaxWidth(Double.MAX_VALUE);
        textArea.setMaxHeight(Double.MAX_VALUE);
        textArea.setStyle("-fx-font-size: 24px; " +
                "-fx-font-family: Calibri; " +
                "-fx-text-fill: black;");
        textArea.setWrapText(true);
        textArea.setPrefSize(WIDTH - 400, HEIGHT - 200);

        ScrollPane scrollPane = new ScrollPane();
        scrollPane.setContent(textArea);
        scrollPane.setFitToWidth(true);
        scrollPane.setFitToHeight(true);
        scrollPane.setLayoutX(50);
        scrollPane.setLayoutY(50);

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

        // Classify Button
        Button classifyButton = new Button("CLASSIFY TEXT");
        classifyButton.setStyle("-fx-font-size: 26px; " +
                "-fx-font-family: Calibri; " +
                "-fx-text-fill: white; " +
                "-fx-background-color: black; " +
                "-fx-border-color: white;");
        classifyButton.setPrefWidth(200);
        classifyButton.setLayoutX((WIDTH - 300));
        classifyButton.setLayoutY(500);
        classifyButton.setOnAction(e -> {
            String inputText = textArea.getText();
            String result = sendRequest(inputText);
            System.out.println("Result from server: " + result);
            GUI_email.window.getScene().setRoot(new Analysis(inputText, result));
        });

        Button undoButton = new Button("CLEAR TEXT");
        undoButton.setLayoutX((WIDTH - 300));
        undoButton.setLayoutY(300);
        undoButton.setStyle("-fx-font-size: 26px; " +
                "-fx-font-family: Calibri; " +
                "-fx-text-fill: white; " +
                "-fx-background-color: black; " +
                "-fx-border-color: white;");
        undoButton.setPrefWidth(200);
        undoButton.setOnAction(event -> {
            textArea.clear();
        });

        Button insertFileButton = new Button("INSERT FILE");
        insertFileButton.setLayoutX(WIDTH - 300 );
        insertFileButton.setLayoutY(400);
        insertFileButton.setStyle("-fx-font-size: 26px; " +
                "-fx-font-family: Calibri; " +
                "-fx-text-fill: white; " +
                "-fx-background-color: black; " +
                "-fx-border-color: white;");
        insertFileButton.setPrefWidth(200);
        insertFileButton.setOnAction(event -> {
            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("Select Text File");
            fileChooser.getExtensionFilters().addAll(
                    new FileChooser.ExtensionFilter("Text Files", "*.txt")
            );
            File selectedFile = fileChooser.showOpenDialog(null);
            if (selectedFile != null) {
                try (BufferedReader reader = new BufferedReader(new FileReader(selectedFile))) {
                    StringBuilder content = new StringBuilder();
                    String line;
                    while ((line = reader.readLine()) != null) {
                        content.append(line).append("\n");
                    }
                    textArea.appendText(content.toString());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });

        getChildren().addAll(Logo, exit, classifyButton, scrollPane, insertFileButton, undoButton, homeButton);
    }
    private String sendRequest(String text) {
        try {
            URL url = new URL("http://localhost:5000/detect_spam");
            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("POST");
            con.setRequestProperty("Content-Type", "application/json");
            con.setDoOutput(true);
            String jsonInputString = "{\"text\": \"" + text + "\"}";
            try (OutputStream os = con.getOutputStream()) {
                byte[] input = jsonInputString.getBytes("utf-8");
                os.write(input, 0, input.length);
            }
            try (BufferedReader br = new BufferedReader(
                    new InputStreamReader(con.getInputStream(), "utf-8"))) {
                StringBuilder response = new StringBuilder();
                String responseLine = null;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                return response.toString();
            }
        } catch (IOException e) {
            e.printStackTrace();
            return "Error sending request";
        }
    }
}

