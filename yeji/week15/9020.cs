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
            int n = int.Parse(Console.ReadLine());
            bool[] isPrime = Enumerable.Repeat(true, 10001).ToArray();
            int answer = 0;
            StringBuilder sb = new StringBuilder();

            for(int i = 2; i<10001;i++)
            {
                for (int j = i * i; j < 10001; j += i)
                {
                    isPrime[j] = false;
                }
            }
            isPrime[0] = false;
            isPrime[1] = false;
            while (n > 0)
            {
                n--;
                int m = int.Parse(Console.ReadLine());
                for (int i = 2; i <= m / 2; i++)
                {
                    if (isPrime[i] && isPrime[m - i])
                    {
                        answer = i;
                    }
                }
                sb.AppendLine($"{answer} {m - answer}");
            }
            Console.Write(sb.ToString());
        }
    }
}
