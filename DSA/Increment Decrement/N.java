class N{
    public static void main(String arg[]){
       int a = 8; //10
       int b = 12; // 14
       int c = ++a + b++; //9 + 12 = 21
       c--; // 19
       --b;
       int d = c-- + ++b + ++a; //20 + 13 + 10 = 43 (44)
       int e = a + ++b +c + d++; //10 + 14 + 19 + 43 = 86
        System.out.println(++e); // 87

    }
}