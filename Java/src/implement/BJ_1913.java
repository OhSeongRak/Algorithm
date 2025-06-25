package implement;

import java.io.*;
import java.util.*;

public class BJ_1913 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] board = new int[N][N];
        int target = Integer.parseInt(br.readLine());

        board = solution(N, board, target);
        printBoard(N, board);
    }

    public static int[][] solution(int N, int[][] board, int target) {
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
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.printf("%3d", board[i][j]);
            }
            System.out.println();
        }
        System.out.println("===========================================");
    }
}