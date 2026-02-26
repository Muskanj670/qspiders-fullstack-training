class J{
    public static void main(String arg[]){
        int x = 12;
        x = x++; //12
        x = x++; //12
        x = x++; //12
        x = ++x;//13
        x = x++; //13

        System.out.println(x);  //13
    }
}