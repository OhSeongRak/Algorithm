package implement;

import java.io.*;
import java.util.*;

public class BJ_1316 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int result = 0;
        String[] lst = new String[N];
        for (int i = 0; i < N; i++) {
            result += solution(br.readLine().toCharArray());
        }

        System.out.println(result);
    }

    public static int solution(char[] lst) {
        boolean[] alphaList = new boolean[26];
        int N = lst.length;
        alphaList[lst[0] - 'a'] = true;

        for (int i = 1; i < N; i++) {
            if (lst[i] != lst[i - 1] && alphaList[lst[i] - 'a']) {
                return 0;
            }
            alphaList[lst[i] - 'a'] = true;
        }

        return 1;
    }
}
