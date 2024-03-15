using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
namespace baek2
{
    class Program
    {
        class Pair
        {
            public int key { get; }
            public int value { get; }
            public Pair(int key, int value)
            {
                this.key = key;
                this.value = value;
            }
        }
        public static void Main()
        {
            int n = int.Parse(Console.ReadLine());
            while(n>0)
            {
                string[] token = Console.ReadLine().Split();
                int N = int.Parse(token[0]);
                int M = int.Parse(token[1]);

                Queue<Pair> queue = new Queue<Pair>();
                int[] input = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
                
                for(int i = 0; i<N;i++)
                {
                    queue.Enqueue(new Pair(i, input[i]));
                }
                Array.Sort(input);
                int count = 0;
                int num = 0;
                while (true)
                { 
                    
                    Pair firstitem = queue.Dequeue();
                    if (firstitem.value.Equals(input[input.Length - 1 - num]) && firstitem.key == M)
                    {
                        count++;
                        Console.WriteLine(count);
                        break;
                    }
                    else if (firstitem.value.Equals(input[input.Length - 1 - num]))
                    {
                        count++;
                        num++;
                        continue;
                    }
                    queue.Enqueue(firstitem);                    
                }
                n--;
            }
        }
    }
}
