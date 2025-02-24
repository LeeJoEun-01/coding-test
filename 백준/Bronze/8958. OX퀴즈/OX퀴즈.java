import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int num = 0;
        String str = " ";

        Scanner sc = new Scanner(System.in);
        
        //System.out.println("테스트 케이스 개수를 입력해주세요! ");
        num = sc.nextInt();
        
        int[] result = new int[num];

        for( int i=0; i<num; i++) {
            //System.out.println("OX배열 테스트 케이스를 입력해주세요! ");
            str = sc.next();
            String[] arr;
            arr = str.split("");
            // System.out.println(arr.length);
            int score = 0;
            int sum = 0;
            for( int j=0; j<arr.length; j++) {
                char target = str.charAt(j);
                if( target == 'O') {
                    score += 1;
                } else {
                    score = 0;
                }
                sum += score;
                //System.out.println(sum);
            }
            result[i] = sum ;
        }
        sc.close();

        //System.out.println("정답");
        for (int answer : result) {
            System.out.println(answer);
        }
    }
}