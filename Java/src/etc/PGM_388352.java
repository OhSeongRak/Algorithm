package etc;

import java.util.Arrays;
import java.util.HashSet;

public class PGM_388352 {
    public static void main(String[] args) {
        int n = 15;
        int[][] q = {{2, 3, 9, 12, 13}, {1, 4, 6, 7, 9}, {1, 2, 8, 10, 12}, {6, 7, 11, 13, 15}, {1, 4, 10, 11, 14}};
//                {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {3, 7, 8, 9, 10}, {2, 5, 7, 9, 10}, {3, 4, 5, 6, 7}};
        int[] ans = {2, 1, 3, 0, 1};
        System.out.println(solution(n, q, ans));
    }

    public static boolean check(HashSet<Integer> set) {

        for (int i = 0; i < Q.length; i++) {
            int count = 0;
            for (int j = 0; j < 5; j++) {
                if (set.contains(Q[i][j])) {
                    count++;
                }
            }
            if (count != ANS[i])
                return false;
        }

        return true;
    }

    public static void combination(int index, int cur, HashSet<Integer> set) {
        if (index == 5) {
            if (check(set))
                result++;
            return;
        }
        for (int i = cur; i <= N; i++) {
            set.add(i);
            combination(index + 1, i + 1, set);
            set.remove(i);
        }
    }

    static int N;
    static int[][] Q;
    static int[] ANS;
    static int result = 0;

    public static int solution(int n, int[][] q, int[] ans) {
        N = n;
        Q = q;
        ANS = ans;

        combination(0, 1, new HashSet<>());

        return result;
    }
}
