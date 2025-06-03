import java.io.*;
import java.util.*;

public class template {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] lst = new int[N];
        for (int i = 0; i < N; i++) {
            lst[i] = Integer.parseInt(st.nextToken());
        }

        StringBuilder sb = new StringBuilder();
        for (int num : lst) {
            sb.append(num).append("\n");
        }
        sb.append(solution());
        System.out.print(sb.toString());
    }

    public static String solution() {
        return "";
    }
}