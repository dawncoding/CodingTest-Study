using System;
using System.Collections.Generic;
using System.Text;
namespace baek2
{
    class Program
    {
        static int[,] input;
        static StringBuilder result = new StringBuilder();
        public static void cd(int x, int y, int size)
        {
            int num = input[y, x];
            bool isSame = true;
            for (int i = y; i < size+ y; i++)
            {
                for (int j = x; j < size+x; j++)
                {
                    if(num != input[i,j])
                    {
                        isSame = false;
                        break;
                    }
                }
                if (!isSame) break;
            }

            if(isSame)
            {
                result.Append(num);
                return;
            }
            result.Append("(");
            int newSize = size / 2;
            cd(x, y, newSize);
            cd(x + newSize , y, newSize);
            cd(x, y + newSize , newSize);
            cd(x + newSize, y + newSize, newSize);
            result.Append(")");
        }
        public static void Main()
        {
            int n = int.Parse(Console.ReadLine());
            input = new int[n + 1, n + 1];
            for (int i = 0; i < n; i++)
            {
                string s = Console.ReadLine();
                for (int j = 0; j < n; j++)
                {
                    input[i, j] = int.Parse(s[j].ToString());
                }
            }

            cd(0, 0, n);
            Console.WriteLine(result.ToString());
        }
    }
}