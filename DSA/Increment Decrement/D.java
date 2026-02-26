class D{
    public static void main(String arg[]){
        int a = 12;
        int b = a++; // 13 12
        b++; //13
        int c = a++ + --b; //14 12 25
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);


    }
}