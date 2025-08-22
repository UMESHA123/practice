package pattern;

public class pattern14 {
    public static void main(String[] args) {
        int n = 5;

        char s = 'A';
        for(int i=1;i<n+1;i++){
            for(int j=0;j<i;j++){
                System.out.print(s);
            }
            s++;
            System.out.println();
        }
    }
    
}
