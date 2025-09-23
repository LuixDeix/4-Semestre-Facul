public class Program
{
    public struct Item
    {
        public string nome;
        public int quantidade;
        public double preco;
    }

    public static void atualizaItem(ref Item item, int novaQuantidade, double novoPreco)
    {
        item.quantidade = novaQuantidade;
        item.preco = novoPreco;
        Console.WriteLine($"item '{item.nome}' atualizado");
    }

    public static void Main(string[] args)
    {
        var inventario = new Dictionary<string, Item>();
        
        Item item1 = new Item { nome = "notebook", quantidade = 10, preco = 2500.00 };
        inventario[item1.nome] = item1;

        Item item2 = new Item { nome = "mouse", quantidade = 50, preco = 50.00 };
        inventario[item2.nome] = item2;
        
        Console.WriteLine("inventario antes da atualizacao:");
        foreach (var item in inventario.Values)
        {
            Console.WriteLine($"-> {item.nome}, qtd: {item.quantidade}, preco: {item.preco:C}");
        }

        Console.WriteLine("\n~ uuu atualizando inventariooo uuuuu~");
        
        Item i = inventario["notebook"];
        atualizaItem(ref i, 8, 2450.00);
        inventario["notebook"] = i;

        Item j = inventario["mouse"];
        atualizaItem(ref j, 45, 45.00);
        inventario["mouse"] = j;

        Console.WriteLine("\ninventario depois da atualizacao:");
        foreach (var item in inventario.Values)
        {
            Console.WriteLine($"-> {item.nome}, qtd: {item.quantidade}, preco: {item.preco:C}");
        }
    }
}