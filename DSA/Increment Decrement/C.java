class C{
    public static void main(String arg[]){
        int a = 20;
        a++; //21
        int b = a++; // 21 22
        int c = ++b; //22 22
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);


    }
}