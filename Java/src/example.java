import java.io.*;
import java.util.*;

public class example {
    public static void main(String[] args) throws IOException {

        // 방법 1: StringTokenizer 사용 (가장 추천!)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int rows = 3; // 행의 개수
        int cols = 3; // 열의 개수
        int[][] arr1 = new int[rows][cols];

        for (int i = 0; i < rows; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < cols; j++) {
                arr1[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.out.println("방법 1 결과:");
        printArray(arr1);
        System.out.println();

        // 방법 2: split 사용
        br = new BufferedReader(new InputStreamReader(System.in));
        int[][] arr2 = new int[rows][cols];

        for (int i = 0; i < rows; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 0; j < cols; j++) {
                arr2[i][j] = Integer.parseInt(line[j]);
            }
        }

        System.out.println("방법 2 결과:");
        printArray(arr2);
        System.out.println();

        // 방법 3: split + Stream 사용 (한 줄로!)
        br = new BufferedReader(new InputStreamReader(System.in));
        int[][] arr3 = new int[rows][cols];

        for (int i = 0; i < rows; i++) {
            arr3[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }

        System.out.println("방법 3 결과:");
        printArray(arr3);
        System.out.println();

        // 방법 4: Scanner 사용 (간단하지만 느림)
        /*
        Scanner sc = new Scanner(System.in);
        int[][] arr4 = new int[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                arr4[i][j] = sc.nextInt();
            }
        }

        System.out.println("방법 4 결과:");
        printArray(arr4);
        sc.close();
        */

        br.close();
    }

    // 2차원 배열 출력 함수
    public static void printArray(int[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}