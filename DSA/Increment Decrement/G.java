class G{
    public static void main(String arg[]){
        int a = 10;
        int b = 5;
        int c = a-- - --b + a++ + ++b;
        System.out.println(c); //10 - 4 + 9 + 5
    }
}