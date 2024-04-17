using System.Collections.Generic;
using System;


namespace baek2
{
    class Program
    {
        static string[] input;
        static int n;
        static bool[] visited;
        static List<string> ans = new List<string>();

        public static bool check(int i, int j, string s)
        {
            if (s == "<") return i < j;
            else return i > j;
        }
        public static void dfs(int cnt, string num)
        {

            if (cnt == n + 1)
            {
                ans.Add(num);
                return;
            }
            for (int i = 0; i < 10; i++)
            {
                if (!visited[i])
                {
                    if (cnt == 0 || check(int.Parse(num[cnt - 1].ToString()), i, input[cnt - 1]))
                    {
                        visited[i] = true;
                        dfs(cnt + 1, num + i.ToString());
                        visited[i] = false;
                    }
                }
            }
        }
        public static void Main()
        {
            n = int.Parse(Console.ReadLine());
            input = Console.ReadLine().Split();
            visited = new bool[10];

            dfs(0, "");
            ans.Sort();

            Console.WriteLine(ans[ans.Count - 1]);
            Console.Write(ans[0]);
        }
    }
}
