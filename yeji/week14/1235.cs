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
            List<string> students = new List<string>();

            for(int i = 0; i<n; i++)
            {
                string input = Console.ReadLine();
                students.Add(input);
            }
            int answer = 1;
           
            string[] numbers = new string[n];
            for (int i = students[0].Length - 1; i >= 0; i--)
            {
                int count = 0;
                for (int j = n-1; j>=0; j--)
                {
                    string number = students[j][i].ToString();
                    numbers[count] = number + numbers[count];
                    count++;
                }
                if (numbers.Distinct().Count() == students.Count())
                {
                    Console.Write(answer);
                    return;
                }
                answer++;
            }
            Console.Write(0);
        }
    }
}
