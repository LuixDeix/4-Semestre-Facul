public class Program
{
    public struct Cliente
    {
        public string nome;
        public int idade;
    }

    public static void alteraCliente(ref Cliente c, string novoNome, int novaIdade)
    {
        c.nome = novoNome;
        c.idade = novaIdade;
    }

    public static void Main(string[] args)
    {
        Cliente cliente = new Cliente();
        
        Console.Write("digite o nome do cliente: ");
        cliente.nome = Console.ReadLine();
        
        Console.Write("digite a idade do cliente: ");
        cliente.idade = int.Parse(Console.ReadLine());
        
        Console.WriteLine("\ndados originais:");
        Console.WriteLine($"nome: {cliente.nome}, idade: {cliente.idade}");

        alteraCliente(ref cliente, "joao silva", 35);
        
        Console.WriteLine("\ndados alterados:");
        Console.WriteLine($"nome: {cliente.nome}, idade: {cliente.idade}");
    }
}