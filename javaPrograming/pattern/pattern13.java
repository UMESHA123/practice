package pattern;

public class pattern13 {
    public static void main(String[] args) {
        int n = 5;
        

        for(int i=n;i>0;i--){
            char s = 'A';
            for(int j=0;j<i;j++){
                System.out.print(s+ " ");
                s++;
            }
            System.out.println();
        }
    }
}
