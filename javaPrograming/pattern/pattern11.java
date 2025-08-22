package pattern;

public class pattern11 {
    public static void main(String[] args) {
        int n = 5;
        int num = 1;

        for(int i=1;i<n+1;i++){
            for(int j=0;j<i;j++){
                System.out.print(num + " ");
                num = num + 1;
            }
            System.out.println();
        }
    }
}
