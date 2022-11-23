public class prac {
    public static void main(String[] args) {
//     int i1 = 0x11, i2 = 5;
//     final int ONE = 1;
//     char c1 = 'a';
//     float f1 = 1.5f;
//     double d1 = 2.8;
//     boolean b1 = true;
//     System.out.println("(int)c1 + ONE = " + (int)c1 + ONE);
//     System.out.printf("(c1 + ONE) %d\n", c1 + ONE);
//     System.out.printf("(c1 + ONE) = %c\n", c1 + ONE);
        int sum = 0;
        for(int i = 0; i <5; i++) {
            if( i % 3 == 0)
            continue;
            sum += i;
        }
        System.out.println(sum);
   } 
}
