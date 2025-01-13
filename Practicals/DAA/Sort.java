package DAA;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.Scanner;

public class Sort {

    int[] bubbleSort(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] > nums[j]) {
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
            }
        }
        return nums;
    }

    int[] selectionSort(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int min_idx = i;
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] < nums[min_idx]) {
                    min_idx = j;
                }
            }
            if (min_idx != i) {
                int temp = nums[i];
                nums[i] = nums[min_idx];
                nums[min_idx] = temp;
            }
        }
        return nums;
    }

    public static void main(String[] args) {
        Random rand = new Random();
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the size of the array to be generated: ");
        int len = input.nextInt();

        System.out.print("Enter the upper limit of the numbers to be generated: ");
        int lim = input.nextInt();

        System.out.print("Enter the number of times to run: ");
        int no = input.nextInt();

        // Create file writers for the sorting times
        try (FileWriter bubbleWriter = new FileWriter("bubSort.txt");
             FileWriter selectionWriter = new FileWriter("selSort.txt")) {

            while (no > 0) {
                no--;

                int[] nums = new int[len];
                int[] numsCopy = new int[len];

                // Generate random numbers and write to file
                File obj = new File("Sample.txt");
                try (FileWriter writer = new FileWriter("Sample.txt")) {
                    for (int i = 0; i < len; i++) {
                        int number = rand.nextInt(lim);
                        writer.write(number + " ");
                    }
                } catch (IOException e) {
                    System.out.println("Error writing to file: " + e.getMessage());
                }

                // Read numbers from file
                try (Scanner reader = new Scanner(obj)) {
                    for (int i = 0; i < len; i++) {
                        if (reader.hasNextInt()) {
                            nums[i] = reader.nextInt();
                        }
                    }
                } catch (IOException e) {
                    System.out.println("Error reading from file: " + e.getMessage());
                }

                // Copy array for selection sort
                System.arraycopy(nums, 0, numsCopy, 0, nums.length);

                Sort sort = new Sort();

                // Measure Bubble Sort time
                long bubbleStartTime = System.nanoTime();
                sort.bubbleSort(nums);
                long bubbleEndTime = System.nanoTime();
                long bubbleTime = bubbleEndTime - bubbleStartTime;
                bubbleWriter.write(bubbleTime + " ns\n");

                // Measure Selection Sort time
                long selectionStartTime = System.nanoTime();
                sort.selectionSort(numsCopy);
                long selectionEndTime = System.nanoTime();
                long selectionTime = selectionEndTime - selectionStartTime;
                selectionWriter.write(selectionTime + " ns\n");
            }

            System.out.println("Sorting times saved to bubSort.txt and selSort.txt");

        } catch (IOException e) {
            System.out.println("Error writing sorting times to file: " + e.getMessage());
        }

        input.close();
    }
}
