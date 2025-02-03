package DAA;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.Scanner;

public class InsertionMergeSort {

    // Method to perform insertion sort
    int[] insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
        return arr;
    }

    // Method to merge two subarrays
    void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] leftArray = new int[n1];
        int[] rightArray = new int[n2];

        // Copy data to temp arrays
        for (int i = 0; i < n1; i++)
            leftArray[i] = arr[left + i];
        for (int j = 0; j < n2; j++)
            rightArray[j] = arr[mid + 1 + j];

        // Merge the temp arrays back into the original array
        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) {
            if (leftArray[i] <= rightArray[j]) {
                arr[k] = leftArray[i];
                i++;
            } else {
                arr[k] = rightArray[j];
                j++;
            }
            k++;
        }

        // Copy remaining elements of leftArray[]
        while (i < n1) {
            arr[k] = leftArray[i];
            i++;
            k++;
        }

        // Copy remaining elements of rightArray[]
        while (j < n2) {
            arr[k] = rightArray[j];
            j++;
            k++;
        }
    }

    // Method to perform merge sort
    void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    public static void main(String[] args) {
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the size of the array to be generated: ");
        int len = scanner.nextInt();

        System.out.print("Enter the upper limit of the numbers to be generated: ");
        int upperLimit = scanner.nextInt();

        System.out.print("Enter the number of times to run: ");
        int iterations = scanner.nextInt();

        try (FileWriter insertionSortTimes = new FileWriter("insertionSortTimes.txt");
             FileWriter mergeSortTimes = new FileWriter("mergeSortTimes.txt");
             FileWriter sortedInsertion = new FileWriter("SortedInsertion.txt");
             FileWriter sortedMerge = new FileWriter("SortedMerge.txt")) {

            while (iterations > 0) {
                iterations--;

                int[] array = new int[len];
                int[] copyArray = new int[len];
                File sampleFile = new File("ArrayPrac2");

                // Generate random numbers and write to file
                try (FileWriter sampleWriter = new FileWriter(sampleFile)) {
                    for (int i = 0; i < len; i++) {
                        int randomNum = random.nextInt(upperLimit);
                        sampleWriter.write(randomNum + " ");
                    }
                } catch (IOException e) {
                    System.out.println("Error writing to file: " + e.getMessage());
                    return;
                }

                // Read numbers from file into the array
                try (Scanner fileScanner = new Scanner(sampleFile)) {
                    for (int i = 0; i < len && fileScanner.hasNextInt(); i++) {
                        array[i] = fileScanner.nextInt();
                    }
                } catch (IOException e) {
                    System.out.println("Error reading from file: " + e.getMessage());
                    return;
                }

                // Create a copy of the array for merge sort
                System.arraycopy(array, 0, copyArray, 0, array.length);

                InsertionMergeSort sorter = new InsertionMergeSort();

                // Measure time for insertion sort
                long startInsertion = System.nanoTime();
                sorter.insertionSort(array);
                long endInsertion = System.nanoTime();
                insertionSortTimes.write(len + ":" + (endInsertion - startInsertion) + " ns\n");
                sortedInsertion.write(len + ": ");
                for (int i = 0; i < len; i++) {
                    sortedInsertion.write(array[i] + " ");
                }
                sortedInsertion.write("\n\n");

                // Measure time for merge sort
                long startMerge = System.nanoTime();
                sorter.mergeSort(copyArray, 0, copyArray.length - 1);
                long endMerge = System.nanoTime(); 
                sortedMerge.write(len + ": ");
                mergeSortTimes.write(len + ":" +(endMerge - startMerge) + " ns\n");
                for (int i = 0; i < len; i++) {
                    sortedMerge.write(copyArray[i] + " ");
                }
                sortedMerge.write("\n\n");
                
                len +=500;
            }

            System.out.println("Sorting times saved to insertionSortTimes.txt and mergeSortTimes.txt");
        } catch (IOException e) {
            System.out.println("Error writing sorting times to file: " + e.getMessage());
        }

        scanner.close();
    }
}
