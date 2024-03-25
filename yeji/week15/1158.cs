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
            int[] input = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int N = input[0];
            int K = input[1];
            StringBuilder sb = new StringBuilder();
            List<int> answer = new List<int>();
            for(int i = 0; i<N; i++)
            {
                answer.Add(i+1);
            }
            int count = 0;
            int len = 0;
            sb.Append("<");
            while(len < N)
            {
                if((count + 1) % K == 0)
                {
                    sb.Append(answer[count]);
                    if (len < N - 1)
                        sb.Append(", ");
                    len++;
                }
                else
                {
                    answer.Add(answer[count]);
                }
                count++;
            }
            sb.Append(">");
            Console.WriteLine(sb.ToString());
        }
    }
}
