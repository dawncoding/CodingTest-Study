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

            string[] input = Console.ReadLine().Split();
            int[] dp = new int[input.Length + 1];
            int[] v = new int[input.Length + 1];
            for(int i = 1; i <= input.Length;i++)
            {
                v[i] = int.Parse(input[i - 1]);
            }

            for(int i = 1; i<= n;i++)
            {
                for(int j = 1; j<=i; j++)
                {
                    dp[i] = Math.Max(dp[i], dp[i - j] + v[j]);
                }
            }

            Console.WriteLine(dp[n]);
        }
    }
}
