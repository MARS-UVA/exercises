import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.*;

public class Main {

    public static byte[] readFileToByteArray(String filePath) throws IOException {
        File file = new File(filePath);
        byte[] fileData = new byte[(int) file.length()];
        try (FileInputStream fis = new FileInputStream(file)) {
            fis.read(fileData);
        }
        return fileData;
    }

    public static int[][] generateRandomGrid() {
        Random random = new Random();
        int numRows = random.nextInt(8) + 3;
        int numCols = random.nextInt(8) + 3;

        // Create the grid with all 1s
        int[][] grid = new int[numRows][numCols];
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                grid[i][j] = 1;
            }
        }

        int numZeros = random.nextInt(numRows * numCols / 2) + 1;

        for (int k = 0; k < numZeros; k++) {
            int row = random.nextInt(numRows);
            int col = random.nextInt(numCols);
            grid[row][col] = 0;
        }

        return grid;
    }

    public static void main(String[] args) {
        // Task 1 output
        System.out.println("Testing MaxFinder:");
        System.out.println("max of [6, 4, 3] is "
                + MaxFinder.max(6, 4, 3));

        // Task 3 output
        try {
            ProcessBuilder processBuilder = new ProcessBuilder("bash", "binMessage.sh");
            byte[] byteArray = readFileToByteArray("../../robot_data.bin");
            double[] returnValue = MessageArrayParser.parseByteArray(byteArray);
            System.out.println(Arrays.toString(returnValue));
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Task 4 output
        int[][] grid = generateRandomGrid();
        AllPossiblePaths.countAllPossiblePaths(grid);
    }
}