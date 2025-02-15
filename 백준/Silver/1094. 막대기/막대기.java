import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        int x = 0;
        int stick = 64;
        int count = 1;

        Scanner sc = new Scanner(System.in);
        x = sc.nextInt();
        sc.close();
        
        // X cm == stick의 길이
        while( x != stick){  // 조건문이 true 일 때 실행 false면 종료
            if( x < stick){
                stick = stick/2;
            } else{
                x = x - stick;
                count ++;
            }
        }

        System.out.println(count);
    }


}
