class I{
    public static void main(String arg[]){
        int a = 5;
        int b = 10;
        int c = a-- + ++b - b-- + ++a;
        System.out.println(c); //5 + 11 - 11 + 5
    }
}