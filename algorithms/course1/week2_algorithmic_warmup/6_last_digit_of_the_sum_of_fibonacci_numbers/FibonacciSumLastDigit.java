import java.util.*;

public class FibonacciSumLastDigit {
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

    private static long getFibonacciSumNaive(long n) {
        if (n <= 1)
            return n;

        long period_length = getPeriodLength(10);
        // System.out.println(period_length);
        long remainder = (long) n % period_length;

        if (remainder == 0) return 0;

        long previous = 0;
        long current  = 1;
        long sum      = 1;

        for (long i = 2; i <= remainder; ++i) {
            long tmp_previous = previous;
            previous = current;
            current = (tmp_previous + current) % 10;
            sum += current;
        }

        return sum % 10;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        long s = getFibonacciSumNaive(n);
        System.out.println(s);
    }
}
