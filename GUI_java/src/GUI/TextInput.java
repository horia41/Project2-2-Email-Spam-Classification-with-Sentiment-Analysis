
package GUI;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

import javafx.scene.Node;
import javafx.scene.control.Button;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextArea;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Background;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.stage.FileChooser;
import javafx.stage.Window;

public class TextInput extends Pane {
    static final int WIDTH = 1920;
    static final int HEIGHT = 1080;
    static final Color BACKGROUND_COLOR = Color.web("#000000");

    TextInput() {
        this.setBackground(Background.fill(BACKGROUND_COLOR));

        ImageView Logo = new ImageView("file:GUI_java/src/GUI/resources/BackGround2.2.png");
        Logo.setRotate(-90.0);
        Logo.setX(1570.0);
        Logo.setY(880.0);
        Logo.setPreserveRatio(true);
        Logo.setFitWidth(300.0);


        TextArea textArea = new TextArea();
        textArea.setPromptText("Enter your text here");
        textArea.setMaxWidth(Double.MAX_VALUE);
        textArea.setMaxHeight(Double.MAX_VALUE);
        textArea.setStyle("-fx-font-size: 24px; -fx-font-family: Calibri; -fx-text-fill: black;");
        textArea.setWrapText(true);
        textArea.setPrefSize(1520.0, 880.0);
        ScrollPane scrollPane = new ScrollPane();
        scrollPane.setContent(textArea);
        scrollPane.setFitToWidth(true);
        scrollPane.setFitToHeight(true);
        scrollPane.setLayoutX(50.0);
        scrollPane.setLayoutY(50.0);


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


        Button exit = new Button("x");
        exit.setLayoutX(1720.0);
        exit.setLayoutY(4.0);
        exit.setOnAction((e) -> {
            System.exit(0);
        });
        exit.setStyle("-fx-font-size: 94px; -fx-font-family: Calibri; -fx-text-fill: white; -fx-background-color: black; -fx-border-color: transparent;");



        Button classifyButton = new Button("CLASSIFY TEXT");
        classifyButton.setStyle("-fx-font-size: 26px; -fx-font-family: Calibri; -fx-text-fill: white; -fx-background-color: black; -fx-border-color: white;");
        classifyButton.setPrefWidth(200.0);
        classifyButton.setLayoutX(1620.0);
        classifyButton.setLayoutY(500.0);
        classifyButton.setOnAction((e) -> {
            String inputText = textArea.getText();
            if(inputText.isEmpty()) {
                System.out.println("Text area is empty");
                return;
            }
            String urlString = "http://127.0.0.1:5000/detect_spam"; // SERVER LINK

            String result = sendRequest(urlString, inputText);
            System.out.println("Result from server: " + result);
            GUI_email.window.getScene().setRoot(new Analysis(inputText, result));
        });


        Button undoButton = new Button("CLEAR TEXT");
        undoButton.setLayoutX(1620.0);
        undoButton.setLayoutY(300.0);
        undoButton.setStyle("-fx-font-size: 26px; -fx-font-family: Calibri; -fx-text-fill: white; -fx-background-color: black; -fx-border-color: white;");
        undoButton.setPrefWidth(200.0);
        undoButton.setOnAction((event) -> {
            textArea.clear();
        });


        Button insertFileButton = new Button("INSERT FILE");
        insertFileButton.setLayoutX(1620.0);
        insertFileButton.setLayoutY(400.0);
        insertFileButton.setStyle("-fx-font-size: 26px; -fx-font-family: Calibri; -fx-text-fill: white; -fx-background-color: black; -fx-border-color: white;");
        insertFileButton.setPrefWidth(200.0);
        insertFileButton.setOnAction((event) -> {
            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("Select Text File");
            fileChooser.getExtensionFilters().addAll(new FileChooser.ExtensionFilter[]{new FileChooser.ExtensionFilter("Text Files", new String[]{"*.txt"})});
            File selectedFile = fileChooser.showOpenDialog((Window)null);
            if (selectedFile != null) {
                try {
                    BufferedReader reader = new BufferedReader(new FileReader(selectedFile));

                    try {
                        StringBuilder content = new StringBuilder();

                        while(true) {
                            String line;
                            if ((line = reader.readLine()) == null) {
                                textArea.appendText(content.toString());
                                break;
                            }

                            content.append(line).append("\n");
                        }
                    } catch (Throwable var8) {
                        try {
                            reader.close();
                        } catch (Throwable var7) {
                            var8.addSuppressed(var7);
                        }

                        throw var8;
                    }

                    reader.close();
                } catch (IOException var9) {
                    var9.printStackTrace();
                }
            }

        });
        this.getChildren().addAll(new Node[]{Logo, exit, classifyButton, scrollPane, insertFileButton, undoButton, homeButton});
    }

    private String sendRequest(String urlString, String textInput) {
        HttpURLConnection con = null;
        try {
            URL url = new URL(urlString);
            con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("POST");
            con.setRequestProperty("Content-Type", "application/json");
            con.setDoOutput(true);

            // Escape newline characters and send the request data
            String jsonInputString = "{\"text\": \"" + textInput.replaceAll("\n", "\\\\n").replaceAll("\"", "\\\"") + "\"}";
            System.out.println("Sending JSON payload: " + jsonInputString);
            try (OutputStream os = con.getOutputStream()) {
                byte[] input = jsonInputString.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }

            // Verify if the response code is HTTP OK (200)
            int responseCode = con.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) {
                // Read the response from the server
                StringBuilder response = new StringBuilder();
                try (BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream(), StandardCharsets.UTF_8))) {
                    String line;
                    while ((line = br.readLine()) != null) {
                        response.append(line.trim());
                    }
                }
                return response.toString();
            } else {
                // Read the error response from the server
                StringBuilder errorResponse = new StringBuilder();
                try (BufferedReader br = new BufferedReader(new InputStreamReader(con.getErrorStream(), StandardCharsets.UTF_8))) {
                    String line;
                    while ((line = br.readLine()) != null) {
                        errorResponse.append(line.trim());
                    }
                }
                System.err.println("Server returned HTTP response code: " + responseCode + " for URL: " + urlString);
                System.err.println("Error response from server: " + errorResponse.toString());
                return "Server error: " + responseCode + " - " + errorResponse.toString();
            }
        } catch (IOException e) {
            e.printStackTrace();
            return "Error sending request";
        } finally {
            if (con != null) {
                con.disconnect();
            }
        }
    }
}