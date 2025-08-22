package pattern;

public class pattern15 {
    public static void main(String[] args) {
        int n = 5;

        for(int i=1;i<n+1;i++){
            char s = 'A';
            for(int j=0;j<(n-i);j++){
                System.out.print(" ");
            }
            for(int j=0;j<i;j++){
                System.out.print((char)(s+j));
            }
            for(int j=i-1;j>0;j--){
                System.out.print((char)(s+j-1));

            }
            System.out.println();
        }
    }
}
