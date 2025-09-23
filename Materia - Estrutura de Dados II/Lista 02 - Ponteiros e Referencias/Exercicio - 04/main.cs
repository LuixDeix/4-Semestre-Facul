public class Program
{
    public static void Main(string[] args)
    {
        int[] memoria = new int[10];

        int a = 0;
        int b = 1;
        int c = 2;
        int p = a;

        memoria[a] = 10;
        memoria[b] = 20;
        memoria[c] = 30;

        Console.WriteLine($"a = {memoria[a]} (pos: {a})");
        Console.WriteLine($"b = {memoria[b]} (pos: {b})");

        Console.WriteLine($"\n    • ponteiro p aponta para a pos {p}, valor: {memoria[p]}");

        p = b;
        Console.WriteLine($"    • ponteiro p aponta para a pos {p}, valor: {memoria[p]}");

        Console.WriteLine("\n~ =-= manipulando valor usando ponteiro =-= ~");
        memoria[p] = 50;
        Console.WriteLine($"    • valor em b agora é: {memoria[b]}");
    }
}