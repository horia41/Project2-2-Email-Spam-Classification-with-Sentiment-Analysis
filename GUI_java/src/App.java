import GUI.GUI_email;

import java.io.IOException;

/**
 * Acts as an entry point to the Application.
 */
public class App {
    public static void main(String[] args) {
        // Start the Flask server
        Thread flaskThread = new Thread(() -> startFlaskServer());
        flaskThread.start();

        // Launch the GUI
        GUI_email.main(args);
    }

    private static void startFlaskServer() {
        try {
            // Create a new process to run the Flask server
            Process process = Runtime.getRuntime().exec("python /path/to/your/app.py");
            System.out.println("Flask server has started.");

            // Wait for the process to finish
            process.waitFor();
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
            System.out.println("Flask server has NOT started.");
        }
    }
}
