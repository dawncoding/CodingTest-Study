using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
namespace baek2
{
    class Program
    {
        public static void Main()
        {
            int[] NK = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int N = NK[0];
            int K = NK[1];

            int[] weight = new int[N + 1];
            int[] value = new int[N + 1];

            for(int i =0; i<N;i++)
            {
                int[] WV = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
                weight[i] = WV[0];
                value[i] = WV[1];
            }
            int[,] dp = new int[N+1, K+1];

            for (int i = 1; i <= N; i++)
            {
                for (int j = 1; j <= K; j++)
                {
                    if (weight[i-1] > j)
                        dp[i,j] = dp[i - 1, j];
                    else
                        dp[i,j] = Math.Max(dp[i-1, j], dp[i-1, j-weight[i-1]] + value[i-1]);
                }
            }
            Console.Write(dp[N,K]);
        }
    }
}
