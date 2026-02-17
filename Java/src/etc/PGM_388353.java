package etc;

import java.io.IOException;
import java.util.*;

public class PGM_388353 {
    public static void main(String[] args) throws IOException {
        String[] storage = {"AZWQY", "CAABX", "BBDDA", "ACACA"};
        String[] requests = {"A", "BB", "A"};
        System.out.println(solution(storage, requests));
    }

    public static boolean inRange(int r, int c) {
        return 0 <= r && r < R && 0 <= c && c < C;
    }

    public static void zigcar(List<int[]> removes, char req) {
        Queue<int[]> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[R][C];
        visited[0][0] = true;
        queue.add(new int[]{0, 0});

        while (!queue.isEmpty()) {
            int r = queue.peek()[0];
            int c = queue.poll()[1];

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (!inRange(nr, nc) || visited[nr][nc])
                    continue;
                if (board[nr][nc] == req) {
                    visited[nr][nc] = true;
                    removes.add(new int[]{nr, nc});
                }
                if (board[nr][nc] == '0') {
                    visited[nr][nc] = true;
                    queue.add(new int[]{nr, nc});
                }
            }
        }
    }

    public static void forkrain(List<int[]> removes, char req) {
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (board[r][c] == req)
                    removes.add(new int[]{r, c});
            }
        }
    }

    public static void printBoard(char[][] board) {
        for (int i = 0; i < R; i++) {
            System.out.println(board[i]);
        }
        System.out.println("============================");
    }

    static int R;
    static int C;
    static char[][] board;
    static int[] dr = {0, 1, 0, -1};
    static int[] dc = {1, 0, -1, 0};

    public static int solution(String[] storage, String[] requests) {
        R = storage.length + 2;
        C = storage[0].length() + 2;
        board = new char[R][C];

        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (r == 0 || c == 0 || r == R - 1 || c == C - 1)
                    board[r][c] = '0';
                else
                    board[r][c] = storage[r - 1].charAt(c - 1);
            }
        }

        for (String req : requests) {
            List<int[]> removes = new ArrayList<>();
            if (req.length() == 1) {
                zigcar(removes, req.charAt(0));
            } else {
                forkrain(removes, req.charAt(0));
            }
            for (int[] pos : removes) {
                board[pos[0]][pos[1]] = '0';
            }
        }

        int answer = 0;
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (board[r][c] != '0')
                    answer++;
            }
        }

        return answer;
    }
}
