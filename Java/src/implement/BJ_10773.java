package implement;

import java.io.*;
import java.util.*;

public class BJ_10773 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num == 0) {
                stack.pop();
            } else {
                stack.push(num);
            }
        }

        int result = 0;
        int size = stack.size();
        for (int i = 0; i < size; i++) {
            result += stack.pop();
        }

        System.out.println(result);

    }
}