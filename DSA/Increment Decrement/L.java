class L{
    public static void main(String arg[]){
       int a = 12;
       int b = a++; //12
       b++;
       int c = a++ + --b; // 13+ 12 = 25
       int d = a++ + ++b + c++; //14 + 13 + 25 = 52
       d++; //53
       c--; //25
        System.out.println(a); //15
        System.out.println(b); //13
        System.out.println(c); // 25
        System.out.println(d); // 53

    }
}