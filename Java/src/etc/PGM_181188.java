package etc;

import java.util.Arrays;

public class PGM_181188 {
    public static void main(String[] args) {
        int[][] targets = {{4, 5}, {4, 8}, {10, 14}, {11, 13}, {5, 12}, {3, 7}, {1, 4}};
        System.out.println(solution(targets));
    }

    public static int solution(int[][] targets) {
        int answer = 0;
        Arrays.sort(targets, (a, b) -> a[1] - b[1]);

        int cur = 0;
        for (int i = 0; i < targets.length; i++) {
            if (targets[i][0] >= cur) {
                answer++;
                cur = targets[i][1];
            }
        }
        return answer;
    }
}
