package etc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class BJ_9012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for(int i = 0; i < N; ++i) {
            System.out.println(solution(br.readLine()));
        }

    }

    public static String solution(String str) {
        Stack<Character> stack = new Stack();

        for(char c : str.toCharArray()) {
            if (c == '(') {
                stack.add(c);
            }

            if (c == ')') {
                if (stack.empty()) {
                    return "NO";
                }

                if ((Character)stack.peek() == '(') {
                    stack.pop();
                } else {
                    stack.add(c);
                }
            }
        }

        if (stack.empty()) {
            return "YES";
        } else {
            return "NO";
        }
    }
}
