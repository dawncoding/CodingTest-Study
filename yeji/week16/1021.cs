using System;
using System.Collections.Generic;

namespace baek2
{
    class Program
    {
        public static void Main()
        {
            int count = 0;
            List<int> dequeue = new List<int>();
            string[] input = Console.ReadLine().Split();           
            int n = int.Parse(input[0]);
            int m = int.Parse(input[1]);
            for (int i = 1; i <= n; ++i)
                dequeue.Add(i);

            string[] input2 = Console.ReadLine().Split();
            List<int> targets = new List<int>();
            for (int i = 0; i < input2.Length; i++)
                targets.Add(int.Parse(input2[i]));

            for (int i = 0; i < m; i++)
            {
                int index = dequeue.IndexOf(targets[0]);
                if (index <= dequeue.Count / 2) 
                {
                    for (int j = 0; j < index; j++) 
                    {
                        int temp = dequeue[0];
                        dequeue.RemoveAt(0); 
                        dequeue.Add(temp); 
                        count++; 
                    }
                }
                else
                {
                    for (int j = 0; j < dequeue.Count - index; j++) 
                    {
                        int temp = dequeue[dequeue.Count - 1];
                        dequeue.RemoveAt(dequeue.Count - 1); 
                        dequeue.Insert(0, temp); 
                        count++; 
                    }
                }
                dequeue.RemoveAt(0);
                targets.RemoveAt(0);
            }
            Console.Write(count);
        }
    }
}
