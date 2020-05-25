import java.util.*;

public class FibonacciHuge {
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

    private static long getFibonacciHuge(long n, long m) {
        if (n <= 1)
            return n;

        long periodLength = getPeriodLength(m);

        // System.out.println(periodLength);

        long remainder = (long) n % periodLength;

        if (remainder == 0) return 0;

        // System.out.println(remainder);

        long previous = 0;
        long current  = 1;
        // long fib[] = new long[remainder+1];

        for (long i = 2; i <= remainder; ++i) {
            long tmp_previous = previous;
            previous = current;
            current = (long) ((tmp_previous + current) % m);
            // fib[i] = fib[i-1] + fib[i-2];
            // System.out.println(current);
        }

        return (long) current % m;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        long m = scanner.nextLong();
        System.out.println(getFibonacciHuge(n, m));
    }
}
