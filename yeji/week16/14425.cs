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
            int n = input[0];
            int m = input[1];

            List<string> n_input = new List<string>();
            for(int i = 0; i<n;i++)
            {
                n_input.Add(Console.ReadLine());
            }
           
            int answer = 0;
            string m_input = "";
            while(m>0)
            {
                m--;
                m_input = Console.ReadLine();
                if (n_input.Contains(m_input)) answer++;
            }
            Console.Write(answer);

        }
    }
}
