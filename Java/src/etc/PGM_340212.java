package etc;

public class PGM_340212 {
    public static void main(String[] args) {
        int[] diffs = {1, 99999, 100000, 99995};
        int[] times = {9999, 9001, 9999, 9001};
        long limit = 3456789012L;
        System.out.println(solution(diffs, times, limit));
    }

    public static int solution(int[] diffs, int[] times, long limit) {
        int N = diffs.length;
        int l = 1;
        int r = 100000;

        while (l < r) {
            int level = (l + r) / 2;
            long total = 0;

            for (int i = 0; i < N; i++) {
                if (i == 0)
                    total += times[i];
                else
                    total += (long) Math.max(0, diffs[i] - level) * (times[i - 1] + times[i]) + times[i];
            }

            if (total <= limit) {
                r = level;
            } else {
                l = level + 1;
            }
        }

        return l;
    }
}