using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Program
{
    static void Main()
    {
        while (true)
        {
            Console.WriteLine("Válassz egy lehetőséget:");
            Console.WriteLine("1. Véletlen számok generálása");
            Console.WriteLine("2. Véletlen szövegek generálása");
            Console.WriteLine("3. Számok ellenőrzése a ki.txt-ben");
            Console.WriteLine("4. Szövegek ellenőrzése a ki.txt-ben");
            Console.WriteLine("5. Kilépés");

            var choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    GenerateRandomNumbers();
                    break;
                case "2":
                    GenerateRandomStrings();
                    break;
                case "3":
                    ValidateNumbersFromFile();
                    break;
                case "4":
                    ValidateStringsFromFile();
                    break;
                case "5":
                    return;
                default:
                    Console.WriteLine("Érvénytelen választás. Kérlek próbáld újra.");
                    break;
            }
        }
    }

    static void GenerateRandomNumbers()
    {
        Console.Write("Add meg a számok darabszámát: ");
        int count = int.Parse(Console.ReadLine());

        Console.Write("Add meg az alsó határt: ");
        int min = int.Parse(Console.ReadLine());

        Console.Write("Add meg a felső határt: ");
        int max = int.Parse(Console.ReadLine());

        var random = new Random();
        var numbers = Enumerable.Range(0, count).Select(_ => random.Next(min, max + 1)).ToList();

        File.WriteAllText("ki.txt", string.Join(";", numbers));
        Console.WriteLine("A véletlen számok a ki.txt fájlba lettek írva.");
    }

    static void GenerateRandomStrings()
    {
        Console.Write("Add meg a szövegek darabszámát: ");
        int count = int.Parse(Console.ReadLine());

        const string chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        var random = new Random();

        var strings = Enumerable.Range(0, count).Select(_ =>
        {
            int length = random.Next(1, 21);
            return new string(Enumerable.Repeat(chars, length).Select(s => s[random.Next(s.Length)]).ToArray());
        }).ToList();

        File.WriteAllText("ki.txt", string.Join(";",Environment.NewLine, strings));
        Console.WriteLine("A véletlen szövegek a ki.txt fájlba lettek írva.");
    }

    static void ValidateNumbersFromFile()
    {
        Console.Write("Add meg a számok darabszámát: ");
        int count = int.Parse(Console.ReadLine());

        Console.Write("Add meg az alsó határt: ");
        int min = int.Parse(Console.ReadLine());

        Console.Write("Add meg a felső határt: ");
        int max = int.Parse(Console.ReadLine());

        var fileContent = File.ReadAllText("ki.txt");
        var numbers = fileContent.Split(';').Select(int.Parse).ToList();

        if (numbers.Count != count || numbers.Any(n => n < min || n > max))
        {
            Console.WriteLine("A fájl tartalma nem felel meg a követelményeknek.");
        }
        else
        {
            Console.WriteLine("A fájl tartalma megfelel a követelményeknek.");
        }
    }

    static void ValidateStringsFromFile()
    {
        Console.Write("Add meg a szövegek darabszámát: ");
        int count = int.Parse(Console.ReadLine());

        var fileContent = File.ReadAllText("ki.txt");
        var strings = fileContent.Split(';').ToList();

        if (strings.Count != count || strings.Any(s => s.Length < 1 || s.Length > 20 || s.Any(c => !char.IsLetter(c))))
        {
            Console.WriteLine("A fájl tartalma nem felel meg a követelményeknek.");
        }
        else
        {
            Console.WriteLine("A fájl tartalma megfelel a követelményeknek.");
        }
    }
}
