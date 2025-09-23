using System;

public class Program
{
    public static void calcula(int a, int b, out int soma, out int produto)
    {
        soma = a + b;
        produto = a * b;
    }

    public static void Main(string[] args)
    {
        int x = 10;
        int y = 5;
        
        calcula(x, y, out int s, out int p);
        
        Console.WriteLine($"soma: {s}");
        Console.WriteLine($"produto: {p}");
    }
}