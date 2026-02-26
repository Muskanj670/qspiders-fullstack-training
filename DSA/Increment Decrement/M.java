class M{
    public static void main(String arg[]){
       int a = 12;
       a++;
       ++a;
       int b = a++;
       b++;
       int c = a++ + --b; //15 + 14 = 29
       c--;
       --b;
       int d= ++a + b++ + --c; // 17 + 13 + 27 = 57
        System.out.println(a); //17
        System.out.println(b); //14
        System.out.println(c); // 27
        System.out.println(d); // 57

    }
}