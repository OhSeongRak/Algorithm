package etc;

import java.io.IOException;

public class PGM_389480 {
    public static void main(String[] args) throws IOException {
        int[][] info = {{1, 2}, {2, 3}, {2, 1}};
        int n = 4;
        int m = 4;

        System.out.println(solution(info, n, m));
    }

    public static int solution(int[][] info, int N, int M) {
        int MAX_SIZE = 100000;
        int R = info.length;
        int[][] dp = new int[R][M];

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < M; j++) {
                dp[i][j] = MAX_SIZE;
            }
        }

        dp[0][0] = info[0][0];
        if (info[0][1] < M) {
            dp[0][info[0][1]] = 0;
        }

        for (int r = 1; r < R; r++) {
            for (int m = 0; m < M - info[r][1]; m++) {
                dp[r][m + info[r][1]] = dp[r - 1][m];
            }
            for (int m = 0; m < M; m++) {
                dp[r][m] = Integer.min(dp[r][m], dp[r - 1][m] + info[r][0]);
            }
        }

        int answer = MAX_SIZE;
        for (int m = 0; m < M; m++) {
            answer = Integer.min(answer, dp[R - 1][m]);
        }

        return answer < N ? answer : -1;
    }
}
