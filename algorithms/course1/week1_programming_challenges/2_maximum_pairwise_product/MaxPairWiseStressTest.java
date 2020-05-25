import java.util.*;
import java.io.*;

public class MaxPairWiseStressTest {
    static long getMaxPairwiseProductFast(long[] numbers) {
        long max_product = 0L;
        int n = numbers.length;
        int max_idx_1 = -1;
        int max_idx_2 = -1;

        for (int i = 0; i < n; i++) {
          if (max_idx_1 == -1 || (numbers[i] > numbers[max_idx_1]))
            max_idx_1 = i;
        }

        for (int i = 0; i < n; i++) {
          if (i != max_idx_1 && (max_idx_2 == -1 || (numbers[i] > numbers[max_idx_2]))) {
            max_idx_2 = i;
          }
        }

        max_product = numbers[max_idx_1] * numbers[max_idx_2];

        return max_product;
    }

    static Long getMaxPairwiseProduct(long[] numbers) {
        long max_product = 0L;
        int n = numbers.length;

        for (int first = 0; first < n; ++first) {
            for (int second = first + 1; second < n; ++second) {
                max_product = Math.max(max_product,
                    numbers[first] * numbers[second]);
            }
        }

        return max_product;
    }

    public static void main(String[] args) {
        while(true) {
          int n = (int)(Math.random() * 20000 + 2);
          System.out.println(n);

          long[] arr = new long[n];
          for (int i = 0; i < n; i++) {
            arr[i] = (long)(Math.random() * 200000L);
          }

          for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
          }

          long res1 = getMaxPairwiseProduct(arr);
          long res2 = getMaxPairwiseProductFast(arr);

          if (res1!=res2) {
            System.out.println("\nWrong answer " + res1 + " " + res2);
            break;
          } else {
            System.out.println("\nOK!");
          }
        }
    }
}
