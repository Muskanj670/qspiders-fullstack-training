class H{
    public static void main(String arg[]){
        int a = 5;
        int b = a++ - --a + a-- - --a;
        System.out.println(b); //5 -5 + 5 - 3
    }
}