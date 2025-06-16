package implement;

import java.io.*;
import java.util.*;

public class BJ_1051 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int[][] board = new int[R][C];

        for (int r = 0; r < R; r++) {
            String line = br.readLine();
            for (int c = 0; c < C; c++) {
                board[r][c] = line.charAt(c) - '0';
            }
        }

        System.out.println(solution(R, C, board));
    }

    public static int solution(int R, int C, int[][] board) {
        int MAX_SIZE = Integer.min(R, C);
        int result = 1;

        for (int T = 1; T < MAX_SIZE; T++) {
            for (int r = 0; r < R - T; r++) {
                for (int c = 0; c < C - T; c++) {
                    if (board[r][c] == board[r + T][c] &&
                            board[r][c] == board[r][c + T] &&
                            board[r][c] == board[r + T][c + T])
                        result = T + 1;
                }
            }
        }

        return result * result;
    }
}