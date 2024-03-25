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
            List<double> list = new List<double>();
            Dictionary<double, double> dict = new Dictionary<double, double>();
            double sum = 0;
            for(int i = 0; i<n;i++)
            {
                double m = double.Parse(Console.ReadLine());
                list.Add(m);
                if (dict.ContainsKey(m)) dict[m]++;
                else dict.Add(m, 1);
                sum += m;
            }
            list.Sort();
            var dict2 = dict.OrderByDescending(x => x.Value).ThenBy(x => x.Key).ToDictionary(x => x.Key, x => x.Value);
            double answer = 0;
            if(dict2.Count > 1)
            {
                if (dict2.Values.ElementAt(1) == dict2.Values.ElementAt(0)) answer = dict2.Keys.ElementAt(1);
                else answer = dict2.Keys.ElementAt(0);
            }
            else answer = dict2.Keys.ElementAt(0);
            Console.WriteLine((int)Math.Round(sum / n));
            Console.WriteLine((int)list[n/2]);
            Console.WriteLine((int)answer);
            Console.Write((int)(list[n-1]-list[0]));
        }
    }
}
