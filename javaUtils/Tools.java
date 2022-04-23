package javaUtils;

import java.util.Arrays;

public class Tools {

    public static void print(String a) {
        System.out.print(a);
    }

    public static <T> void print(T[] arr) {
        if(arr==null) {
            print("null");
            return;
        }
        print("{");
        for(T t :arr) {
            print(t+", ");
        }
        print("}");
    }

    public static void print(int[] arr) {
        print(Arrays.stream(arr).boxed().toArray());
    }

    public static void print(boolean[] arr) {
        for(boolean b:arr) {
            print(b+", ");
        }
    }

    public static <T> void print(T[][] arr) {
        print("{");
        for(T[] ts:arr) {
            print(ts);
            print(", ");
        }
        print("}");
    }

    public static void print(int[][] arr) {
        print("{");
        for(int[] is:arr) {
            print(is);
            print(", ");
        }
        print("}");
    }

    public static <T> void println(T[] arr) {
        print(arr);
        print("\n");
    }

    public static void println(int[] arr) {
        print(arr);
        print("\n");
    }

    public static void println(int[][] arr) {
        print(arr);
        print("\n");
    }

    public static void main(String[] args) {
        int[] a={1,2,3};
        println(a);
        int[][] aa={{1,2,3},{3,4,5}};
        println(aa);
        System.out.println("done");
        int[] b={2,3,4,};
    }
}
