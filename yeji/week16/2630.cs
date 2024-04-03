using System;
using System.Collections.Generic;

namespace baek2
{
    class Program
    {
        static int[,] paper;
        static int whiteCount = 0;
        static int blueCount = 0;
        static void dc(int x, int y, int size)
        {
            int firstColor = paper[y, x];

            bool isSame= true;
            for (int i = y; i < y + size; i++)
            {
                for (int j = x; j < x + size; j++)
                {
                    if (paper[i, j] != firstColor)
                    {
                        isSame = false;
                        break;
                    }
                }
                if (!isSame)
                    break;
            }

            if (isSame)
            {
                if (firstColor == 0)
                    whiteCount++;
                else
                    blueCount++;
                return;
            }

            int newSize = size / 2;
            dc(x, y, newSize); // 왼쪽 위
            dc(x + newSize, y, newSize); // 오른쪽 위
            dc(x, y + newSize, newSize); // 왼쪽 아래
            dc(x + newSize, y + newSize, newSize); // 오른쪽 아래
        }
        public static void Main()
        {
            int n = int.Parse(Console.ReadLine());
            paper = new int[n + 1, n + 1];
            for (int i = 0; i < n; i++)
            {
                int[] token = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
                for (int j = 0; j < n; j++)
                {
                    paper[i, j] = token[j];
                }
            }
            dc(0, 0, n);

            Console.WriteLine(whiteCount);
            Console.Write(blueCount);

        }
    }
}
