package GUI;

import javafx.scene.control.Button;
import javafx.scene.control.ScrollPane;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Background;
import javafx.scene.Node;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;
import javafx.stage.Screen;

import java.util.Arrays;

public class Analysis extends Pane {


    private final double WIDTH;
    private final double HEIGHT;

    private static final double MAX_TEXT_WIDTH = Screen.getPrimary().getBounds().getWidth() - 100;
    static final Color BACKGROUND_COLOR = Color.web("#000000");

    public Analysis(String textInput, String result) {
        // Get screen dimensions
        WIDTH = Screen.getPrimary().getBounds().getWidth();
        HEIGHT = Screen.getPrimary().getBounds().getHeight();

        this.setBackground(Background.fill(BACKGROUND_COLOR));


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


        //Text input
        Text text = new Text(textInput);
        text.setWrappingWidth(1700); // Slightly less than the ScrollPane width
        text.setStyle("-fx-font-size: 35px; -fx-font-family: Calibri; -fx-text-fill: white;");
        text.setFill(Color.WHITE);

        ScrollPane scrollPane = new ScrollPane();
        scrollPane.setContent(text);
        scrollPane.setFitToWidth(true);
        scrollPane.setFitToHeight(true);
        scrollPane.setPrefSize(1920, 1080); // Set a preferred size for the ScrollPane
        scrollPane.setLayoutX(100.0);
        scrollPane.setLayoutY(550.0); // Adjusted Y position
        scrollPane.setStyle("-fx-background: transparent; -fx-background-color: transparent;");

        // Text Display
        String[] results = getresult(result);
        Text resultSVM = new Text("SVM: " + results[1]);
        resultSVM.setWrappingWidth(MAX_TEXT_WIDTH);
        resultSVM.setStyle("-fx-font-size: 70px; -fx-font-family: Calibri; -fx-text-fill: white;");
        resultSVM.setFill(Color.WHITE);
        resultSVM.setLayoutX(100.0);
        resultSVM.setLayoutY(200.0);

        Text resultNB = new Text("Naive Bayes: " + results[0]);
        //System.out.println(results[0]);
        resultNB.setWrappingWidth(MAX_TEXT_WIDTH);
        resultNB.setStyle("-fx-font-size: 70px; -fx-font-family: Calibri; -fx-text-fill: white;");
        resultNB.setFill(Color.WHITE);
        resultNB.setLayoutX(100.0);
        resultNB.setLayoutY(350.0);

        Text sentimentScore = new Text("Sentiment Score: " + results[2]);
        //System.out.println(results[2]);
        sentimentScore.setWrappingWidth(MAX_TEXT_WIDTH);
        sentimentScore.setStyle("-fx-font-size: 70px; -fx-font-family: Calibri; -fx-text-fill: white;");
        sentimentScore.setFill(Color.WHITE);
        sentimentScore.setLayoutX(100.0);
        sentimentScore.setLayoutY(500.0);


        getChildren().addAll(new Node[]{exit, homeButton, scrollPane, resultSVM, resultNB,sentimentScore});
    }

    private String[] getresult(String result) {
        result = result.replaceAll("[{}\"]", "");

        String[] parts = result.split(",");
        String spamBayes = "";
        String spamSVM = "";
        String sentimentScore = "";

        System.out.println(Arrays.toString(parts));

        for (String part : parts)
        {
            String[] keyValue = part.split(":");
            System.out.println(Arrays.toString(keyValue));
            if (keyValue.length == 2) {
                String key = keyValue[0].trim();
                String value = keyValue[1].trim();
                if ("spam_Bayes".equals(key)) {
                    spamBayes = value;
                } else if ("spam_SVM".equals(key)) {
                    spamSVM = value;
                }
            }
            else if (keyValue.length == 3)
            {
               sentimentScore = keyValue[keyValue.length-1].trim();
            }

        }
        //System.out.print(spamBayes + " " + spamSVM + " " + sentimentScore);

        return new String[]{spamBayes, spamSVM, sentimentScore};
    }
}
