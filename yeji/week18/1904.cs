using System;


namespace baek2
{
    class Program
    {
        public static void Main()
        {
            int n = int.Parse(Console.ReadLine());

            int[] dp = new int[n + 1];
            dp[0] = 1;
            dp[1] = 2;
            for (int i = 2; i < n; i++)
            {
                dp[i] = (dp[i - 1] + dp[i - 2]) % 15746;
            }

            Console.Write(dp[n - 1]);
        }
    }
}