using System;

public class Program
{
    public static void troca(ref int a, ref int b)
    {
        int temp = a;
        a = b;
        b = temp;
    }

    public static void Main(string[] args)
    {
        int num1 = 10;
        int num2 = 20;

        Console.WriteLine($"antes: num1 = {num1}, num2 = {num2}");
        
        troca(ref num1, ref num2);
        
        Console.WriteLine($"depois: num1 = {num1}, num2 = {num2}");
    }
}