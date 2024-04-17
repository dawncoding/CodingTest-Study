using System;


namespace baek2
{
    class Program
    {
        public static void Main()
        {
            int[] input = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int n = input[0];
            int m = input[1];
            int[] a = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int answer = 0;

            for (int i = 0; i < n; i++)
            {
                int total = 0;
                for (int j = i; j < n; j++)
                {
                    total += a[j];
                    if (total == m)
                    {
                        answer++;
                        break;
                    }

                }
            }
            Console.WriteLine(answer);
        }
    }
}
