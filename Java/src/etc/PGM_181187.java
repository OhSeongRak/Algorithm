package etc;

public class PGM_181187 {
    public static void main(String[] args) {
        int r1 = 2;
        int r2 = 3;
        System.out.println(solution(r1, r2));
    }

    public static long countDot(int r, boolean inside) {
        long size = (long) r * r;
        long total = (long) (r + 1) * 4 - 3; // x or y가 0인 점 개수

        for (long i = 1; i < r; i++) {
            long count = (long) Math.sqrt(size - i * i);
            if (inside && i * i + count * count == size)
                total -= 4;
            total += count * 4;
        }
        return total;
    }

    public static long solution(int r1, int r2) {
        return countDot(r2, false) - countDot(r1, true) + 4;
    }
}
