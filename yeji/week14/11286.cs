using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
namespace baek2
{
    public class Comparer : IComparer<int>
    {
        public int Compare(int x, int y)
        {
            int absX = Math.Abs(x);
            int absY = Math.Abs(y);

            if (absX == absY)
            {
                return x.CompareTo(y);
            }
            return absX.CompareTo(absY);
        }
    }
    class Program
    {
        public static void Main()
        {
            SortedDictionary<int, int> pq = new SortedDictionary<int, int>(new Comparer());

            StringBuilder sb = new StringBuilder();
            int n = int.Parse(Console.ReadLine());

            for (int i = 0; i < n; i++)
            {
                int input = int.Parse(Console.ReadLine());

                if (input == 0 && pq.Count == 0)
                {
                    sb.AppendLine("0");
                }
                else if (input == 0 && pq.Count != 0)
                {
                    int minValue = pq.First().Key;
                    sb.AppendLine(minValue.ToString());
                    if (pq[minValue] > 1)
                    {
                        pq[minValue]--;
                    }
                    else
                    {
                        pq.Remove(minValue);
                    }
                }
                else
                {
                    if (pq.ContainsKey(input))
                    {
                        pq[input]++;
                    }
                    else
                    {
                        pq.Add(input, 1);
                    }
                }
            }
            Console.Write(sb);
        }
    }
}