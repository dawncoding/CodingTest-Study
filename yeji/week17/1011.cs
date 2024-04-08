using System;
using System.Collections.Generic;
using System.Text;

namespace baek2
{
    class Program
    {
        public static void Main()
        {
            int n = int.Parse(Console.ReadLine());
            StringBuilder sb = new StringBuilder();

            while (n > 0)
            {
                n--;
                string[] input = Console.ReadLine().Split();
                int x = int.Parse(input[0]);
                int y = int.Parse(input[1]);
                int d = y - x;
                double v = Math.Floor(Math.Sqrt(d) + 0.5);

                if (d <= v * v) sb.AppendLine((v * 2 - 1).ToString());
                else sb.AppendLine((v * 2).ToString());

            }
            Console.Write(sb.ToString());
        }
    }
}
