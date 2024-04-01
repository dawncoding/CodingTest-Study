using System;
using System.Collections.Generic;
using System.Text;
namespace baek2
{
    class Program
    {
        static string[] input2;
        static bool[] visited;
        static string[] arr;
        static StringBuilder sb = new StringBuilder();
        static int n, m;
        static string vowel = "aeiou";
        static int c_vl = 0;
        static int c_co = 0;
        static string[] count;

        public static void dfs(int index, int depth)
        {
            if (depth == n)
            {
                for (int i = 0; i < n; i++)
                {
                    count[i] = arr[i];
                    if (vowel.Contains(arr[i])) c_vl++;
                    else c_co++;
                }
                if (c_vl >= 1 && c_co >= 2) sb.AppendLine(string.Join("", count));
                c_vl = 0;
                c_co = 0;
                return;
            }
      
            for (int i = index; i<=m;i++)
            {
                if (!visited[i])
                {
                    visited[i] = true;
                    arr[depth] = input2[i-1];
                    dfs(i,depth + 1);
                    visited[i] = false;
                }
            }
                
        }
        public static void Main()
        {
            string[] input = Console.ReadLine().Split();
            n = int.Parse(input[0]);
            m = int.Parse(input[1]);
            visited = new bool[m + 1];
            arr = new string[n+1];
            count = new string[n + 1];
            input2 = Console.ReadLine().Split();
            Array.Sort(input2);
            dfs(1,0);
            Console.WriteLine(sb.ToString());
        }
    }
}