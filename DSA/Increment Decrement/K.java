class K{
    public static void main(String arg[]){
        int x = 12;
        int y = x++ + ++x; // 12 + 14 = 26
        y++; // 27
        int z = ++y; // 28
        int p = x++ - ++y + z++; //14 - 29 + 28 = 13
        System.out.println(x); //15
        System.out.println(y); //29
        System.out.println(z); //29
        System.out.println(p); //13

    }
}