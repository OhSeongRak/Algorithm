package etc;

import java.io.*;
import java.util.*;

public class PGM_389479 {
    public static void main(String[] args) throws IOException {

        int[] players = {
                0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1
        };
        int m = 1;
        int k = 1;

        System.out.println(solution(players, m, k));
    }

    public static int solution(int[] players, int m, int k) {
        int result = 0;
        int cur = 0;
        int[] ret = new int[24 + k];

        for (int i = 0; i < 24; i++) {
            int n = players[i] / m; // 최소 서버 개수

            cur -= ret[i];
            if (n > cur) {
                int extra = n - cur; // 추가 서버 개수
                cur += extra;
                result += extra;
                ret[i + k] += extra;
            }
        }

        return result;
    }
}
