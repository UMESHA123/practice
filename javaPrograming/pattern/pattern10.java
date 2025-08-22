package pattern;

public class pattern10 {
    public static void main(String args[]){
        int n = 5;

        for(int i=1;i<=n;i++){
            for(int j=1;j<=i;j++){
                System.out.print(j+" ");
            }
            for(int k=0;k<2;k++){
                for(int j=0;j<(2*(n-i));j++){
                    System.out.print(" ");
                }
            }
            for(int j=i;j>0;j--){
                System.out.print(j+ " ");
            }
            System.out.println();
        }
    }
}
