package GUI;

import javafx.scene.control.Button;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextArea;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Background;
import javafx.scene.layout.BorderPane;
import javafx.scene.paint.Color;
import javafx.stage.FileChooser;
import javafx.stage.Screen;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

public class TextInput extends BorderPane {

    private final double WIDTH;
    private final double HEIGHT;

    private static final Color BACKGROUND_COLOR = Color.web("#000000");

    public TextInput() {
        // Get screen dimensions
        WIDTH = Screen.getPrimary().getBounds().getWidth();
        HEIGHT = Screen.getPrimary().getBounds().getHeight();

        setBackground(Background.fill(BACKGROUND_COLOR));

        // Logo Image
        ImageView logo = new ImageView("file:GUI_java/src/GUI/resources/BackGround2.2.png");
        logo.setRotate(-90);
        logo.setPreserveRatio(true);
        logo.setFitWidth(300);

        // Top panel with logo and buttons
        Button homeButton = createHomeButton();
        Button exitButton = createExitButton();

        // Text Area
        TextArea textArea = new TextArea();
        textArea.setPromptText("Enter your text here");
        textArea.setStyle("-fx-font-size: 16px; -fx-font-family: Calibri; -fx-text-fill: black;");
        textArea.setWrapText(true);

        ScrollPane scrollPane = new ScrollPane(textArea);
        scrollPane.setFitToWidth(true);
        scrollPane.setFitToHeight(true);

        // Bottom panel with buttons
        Button classifyButton = createClassifyButton(textArea);
        Button clearTextButton = createClearTextButton(textArea);
        Button insertFileButton = createInsertFileButton(textArea);

        // Set layout positions
        setTop(homeButton);
        setCenter(scrollPane);
        setBottom(insertFileButton);
        setLeft(classifyButton);
        setRight(clearTextButton);
    }

    private Button createHomeButton() {
        Button homeButton = new Button();
        ImageView homeImage = new ImageView("file:GUI_java/src/GUI/resources/home22.png");
        homeImage.setPreserveRatio(true);
        homeImage.setFitHeight(40);
        homeButton.setGraphic(homeImage);
        homeButton.setStyle("-fx-border-color: transparent;" + "-fx-background-color: transparent;");
        homeButton.setOnAction(event -> GUI_email.window.getScene().setRoot(new MainMenu()));
        return homeButton;
    }

    private Button createExitButton() {
        Button exitButton = new Button();
        ImageView exitImage = new ImageView("file:GUI_java/src/GUI/resources/cross22.png");
        exitImage.setPreserveRatio(true);
        exitImage.setFitHeight(40);
        exitButton.setGraphic(exitImage);
        exitButton.setStyle("-fx-border-color: transparent;" + "-fx-background-color: transparent;");
        exitButton.setOnAction(e -> System.exit(0));
        return exitButton;
    }

    private Button createClassifyButton(TextArea textArea) {
        Button classifyButton = new Button("CLASSIFY TEXT");
        classifyButton.setStyle("-fx-font-size: 20px; -fx-font-family: Calibri; -fx-text-fill: white; -fx-background-color: black; -fx-border-color: white;");
        classifyButton.setOnAction(e -> {
            String inputText = textArea.getText();
            String urlString = "http://127.0.0.1:5000/detect_spam"; // SERVER LINK

            String result = sendRequest(urlString, inputText);

            if (result == null) {
                System.out.println("Error: result is null");
                return;
            }
            System.out.println("Result from server: " + result);
            GUI_email.window.getScene().setRoot(new Analysis(inputText, result));
        });
        return classifyButton;
    }

    private Button createClearTextButton(TextArea textArea) {
        Button clearTextButton = new Button("CLEAR TEXT");
        clearTextButton.setStyle("-fx-font-size: 20px; -fx-font-family: Calibri; -fx-text-fill: white; -fx-background-color: black; -fx-border-color: white;");
        clearTextButton.setOnAction(event -> textArea.clear());
        return clearTextButton;
    }

    private Button createInsertFileButton(TextArea textArea) {
        Button insertFileButton = new Button("INSERT FILE");
        insertFileButton.setStyle("-fx-font-size: 20px; -fx-font-family: Calibri; -fx-text-fill: white; -fx-background-color: black; -fx-border-color: white;");
        insertFileButton.setOnAction(event -> {
            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("Select Text File");
            fileChooser.getExtensionFilters().add(new FileChooser.ExtensionFilter("Text Files", "*.txt"));
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
        return insertFileButton;
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
