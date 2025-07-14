package implement;

import java.io.*;

public class BJ_1913 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] board = new int[N][N];
        int target = Integer.parseInt(br.readLine());

        board = solution(N, board);
        printBoard(N, board);
        findNumberPosition(N, target, board);
    }

    public static int[][] solution(int N, int[][] board) {
        int cur = N * N;

        for (int start = 0; start <= N / 2; start++) {
            int size = N - start * 2;

            for (int i = 0; i < size - 1; i++) {
                board[start + i][start] = cur--;
            }
            for (int i = 0; i < size - 1; i++) {
                board[N - 1 - start][start + i] = cur--;
            }
            for (int i = 0; i < size - 1; i++) {
                board[N - 1 - start - i][N - 1 - start] = cur--;
            }
            for (int i = 0; i < size - 1; i++) {
                board[start][N - 1 - start - i] = cur--;
            }
        }

        board[N / 2][N / 2] = 1;

        return board;
    }

    public static void printBoard(int N, int[][] board) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sb.append(board[i][j]).append(" ");
            }
            sb.append("\n");
        }

        System.out.print(sb);
    }

    public static void findNumberPosition(int N, int target, int[][] board) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == target) {
                    System.out.printf("%d %d", i + 1, j + 1);
                    return;
                }
            }
        }
    }

}