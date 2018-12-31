package BasicNumbers;

public class NumberAndOperator {
    public static void main(String args[]){
        int a,b;
        a=20;
        b=10;

        System.out.println("sum of a and b is: "+ addition(a,b));
        System.out.println("subtraction of a and b is: "+ subtraction(a,b));
        System.out.println("multiplication of a and b is: "+ multiplication(a,b));
        System.out.println("division of a and b is: "+ division(a,b));
        System.out.println("modulus of a and b is: "+ modulus(a,b));
    }

    static int addition(int a, int b){
        return a+b;
    }

    static int subtraction(int a, int b){
        return a-b;
    }

    static int multiplication(int a, int b){
        return a*b;
    }

    static int division(int a, int b){
        return a/b;
    }

    static int modulus(int a, int b){
        return a%b;
    }
}
