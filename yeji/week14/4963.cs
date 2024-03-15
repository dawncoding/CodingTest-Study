using System;
using System.Collections.Generic;
using System.Linq;
namespace baek2
{
    class Program
    {
        static int[,] graph;
        static int[] dir = { -1, 0, 1};

        public static void DFS(int x, int y)
        {
            graph[x, y] = 0;

            for(int i = 0; i<3; i++)
            {
                for(int j = 0; j<3;j++)
                {
                    int newX = x + dir[i];
                    int newY = y + dir[j];
                    if (graph[newX, newY] == 1)
                    {
                        DFS(newX, newY);
                    }
                }
            }
            
        }
        public static void Main()
        {
            while (true)
            {
                int[] input = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
                int w = input[0];
                int h = input[1];
                if (w == 0 && h == 0) return;
                graph = new int[100, 100];
                for (int i = 1; i <= h; i++)
                {
                    string[] s = Console.ReadLine().Split();
                    for (int j = 1; j <= w; j++)
                    {
                        graph[j, i] = int.Parse(s[j - 1]);
                    }  
                }
                int count = 0;
                for (int i = 1; i <= h; i++)
                {
                    for (int j = 1; j <= w; j++)
                    {
                        if (graph[j, i] == 1)
                        {
                            count++;
                            DFS(j, i);

                        }
                    }
                }
                Console.WriteLine(count);
            }
        }
    }
}

