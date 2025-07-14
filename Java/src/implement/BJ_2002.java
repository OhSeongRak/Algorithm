package implement;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class BJ_2002 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<String> inList = new ArrayList<>();
        List<String> outList = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            String st = br.readLine();
            inList.add(st);
        }
        for (int i = 0; i < N; i++) {
            String st = br.readLine();
            outList.add(st);
        }

        System.out.println(solution(inList, outList));
    }

    public static int solution(List<String> inList, List<String> outList) {
        int cur = 0;
        int answer = 0;

        for (String number : outList) {
            if (number.equals(inList.get(cur))) {
                cur++;
            } else {
                for (int i = cur + 1; i < inList.size(); i++) {
                    if (number.equals(inList.get(i))) {
                        inList.remove(number);
                        answer++;
                        break;
                    }
                }
            }
        }

        return answer;
    }
}