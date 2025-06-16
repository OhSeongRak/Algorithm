package implement;

import java.io.*;
import java.util.*;

public class BJ_4673 {
    public static void main(String[] args) throws IOException {

        int N = 10001;
        boolean[] lst = new boolean[N];
        for (int i = 1; i < N; i++) {
            lst[hab(i)] = true;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < N; i++) {
            if (!lst[i])
                sb.append(i).append("\n");
        }
        System.out.print(sb);
    }

    public static int hab(int N) {
        int result = N;
        while (N > 0) {
            result += N % 10;
            N = N / 10;
        }

        if (result > 10000)
            result = 0;

        return result;
    }
}