class F{
    public static void main(String arg[]){
        int a = 12;
        int b = 20;
        int c = a++ + b++ - ++a - --a;
        System.out.println(c); //12 + 20 - 14 - 13
    }
}