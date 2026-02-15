package etc;

import java.io.*;
import java.util.*;

public class BJ_2164 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        System.out.println(solution(N));
    }

    public static int solution(int N) {
        Deque<Integer> deque = new ArrayDeque<>();

        for (int i = 1; i <= N; i++) {
            deque.add(i);
        }

        while (deque.size() > 1) {
            deque.pollFirst();
            deque.add(deque.pollFirst());
        }

        return deque.pop();
    }
}