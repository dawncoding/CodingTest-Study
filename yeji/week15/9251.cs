using System;

namespace baek2
{
    class Program
    {
        public static void Main()
        {
            string s1 = Console.ReadLine();
            string s2 = Console.ReadLine();
            int max = 0;
            int[,] graph = new int[s1.Length+1,s2.Length+1];

            for(int i = 1; i<=s1.Length;i++)
            {
                for (int j = 1; j <= s2.Length; j++)
                {
                    if (s1[i - 1] == s2[j - 1])
                    {
                        graph[i, j] = graph[i-1, j - 1] + 1;
                        if (max < graph[i, j]) max = graph[i, j];
                    }
                    else
                    {
                        graph[i, j] = Math.Max(graph[i - 1, j], graph[i, j - 1]);
                    }
                }
            }
            Console.Write(max);
        }
    }
}
