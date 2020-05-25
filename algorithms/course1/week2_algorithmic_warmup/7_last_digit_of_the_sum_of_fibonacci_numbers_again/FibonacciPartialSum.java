import java.util.*;

public class FibonacciPartialSum {
    private static long getPeriodLength(long m) {
      if (m < 2) return 1;

      long previous = 0;
      long current = 1;

      for (long i = 0; i < m * m; i++) {
        long tmp_previous = (long) ((previous + current) % m);

        previous = current;
        current = tmp_previous;

        if (current == 1 && previous == 0) return i + 1;
      }

      return 0;
    }

    private static long getFibonacciPartialSum(long from, long to) {
        if (to < 2) return to;

        long sum = 0;

        long current = 0;
        long next  = 1;

        long period_length = getPeriodLength(10);

        long from_remainder = (long) from % period_length;
        long to_remainder = (long) to % period_length;

        if (from_remainder == 0 && to_remainder == 0) return 0;

        long lower_limit = Math.min(from_remainder, to_remainder);
        long upper_limit = Math.max(from_remainder, to_remainder);
        // System.out.println(lower_limit);

        for (long i = 0; i <= upper_limit; ++i) {
            if (i >= lower_limit) {
                System.out.println(current);
                sum += current;
            }

            long new_current = next;
            next = (next + current) % 10;
            current = new_current;
        }

        return sum % 10;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long from = scanner.nextLong();
        long to = scanner.nextLong();
        System.out.println(getFibonacciPartialSum(from, to));
    }
}
