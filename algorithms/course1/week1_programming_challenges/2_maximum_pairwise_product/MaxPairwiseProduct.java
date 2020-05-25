import java.util.*;
import java.io.*;

public class MaxPairwiseProduct {
    static long getMaxPairwiseProduct(long[] numbers) {
        long max_product = 0;
        int n = numbers.length;
        int max_idx_1 = -1;
        int max_idx_2 = -1;

        for (int i = 0; i < n; i++) {
          if (max_idx_1 == -1 || numbers[i] > numbers[max_idx_1])
            max_idx_1 = i;
        }

        for (int i = 0; i < n; i++) {
          if (i != max_idx_1 && (max_idx_2 == -1 || numbers[i] > numbers[max_idx_2]))
            max_idx_2 = i;
        }

        max_product = numbers[max_idx_1] * numbers[max_idx_2];

        return max_product;
    }

    public static void main(String[] args) {

        if (args.length < 1) System.out.println("specify input filename as argument");

        File file = new File(args[0]);


        Scanner reader = null;
        try {
            reader = new Scanner(file);
        } catch (Exception e) {
          System.out.println(e);
        }

        int n = Integer.parseInt(reader.next());

        int i = 0;
        long[] numbers = new long[n];

        while (reader.hasNextLine() && i < n) {
          numbers[i] = (long)reader.nextLong();
          i++;
        }

        System.out.println(getMaxPairwiseProduct(numbers));

        // FastScanner scanner = new FastScanner(System.in);

        // int n = scanner.nextInt();
        // for (int i = 0; i < n; i++) {
        //     numbers[i] = scanner.nextLong();
        // }
    }

    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner(InputStream stream) {
            try {
                br = new BufferedReader(new
                    InputStreamReader(stream));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
          return Long.parseLong(next());
        }
    }

}
