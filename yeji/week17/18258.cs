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
            Queue<int> queue = new Queue<int>();
            StringBuilder sb = new StringBuilder();
            int last = 0;
            while(n>0)
            {
                n--;
                
                string[] input = Console.ReadLine().Split();
                switch(input[0])
                {
                    case "push":
                        queue.Enqueue(int.Parse(input[1]));
                        last = int.Parse(input[1]);
                        break;
                    case "pop":
                        if (queue.Count == 0) sb.AppendLine("-1");
                        else
                        {
                            sb.AppendLine(queue.Dequeue().ToString());
                        }
                        break;
                    case "size":
                        sb.AppendLine(queue.Count.ToString());
                        break;
                    case "empty":
                        sb.AppendLine(queue.Count > 0 ? "0" : "1");
                        break;
                    case "front": 
                        sb.AppendLine(queue.Count > 0 ? queue.Peek().ToString() : "-1");
                        break;
                    case "back":
                        sb.AppendLine(queue.Count > 0 ? last.ToString() : "-1");
                        break;
                        
                }
            }
            Console.Write(sb.ToString());
        }
    }
}
