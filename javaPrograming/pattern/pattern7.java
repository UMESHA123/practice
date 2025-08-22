package pattern;

public class pattern7 {
    public static void main(String args[]){
        int n = 4;
        
        //for space
        //for n *'s
        //for (n+1) *'s

        for(int i=0;i<n+1;i++){
            for(int j=0;j<(n-i);j++){
                System.out.print(" ");
            }
            for(int j=0;j<i;j++){
                System.out.print("*");
            }
            for(int j=0;j<i+1;j++){
                System.out.print("*");
            }
            System.out.println();
        }
        for(int i=n;i>=0;i--){
            for(int j=0;j<n-i;j++){
                System.out.print(' ');
            }
            for(int j=0;j<i;j++){
                System.out.print("*");
            }
            for(int j=0;j<i+1;j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
