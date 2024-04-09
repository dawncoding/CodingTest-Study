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
            while (n > 0)
            {
                n--;
                string[] s = Console.ReadLine().Split();

                int x1 = int.Parse(s[0].ToString());
                int y1 = int.Parse(s[1].ToString());
                int r1 = int.Parse(s[2].ToString());
                int x2 = int.Parse(s[3].ToString());
                int y2 = int.Parse(s[4].ToString());
                int r2 = int.Parse(s[5].ToString());

                int sub = Math.Abs(r1 - r2);
                double d = Math.Pow(MathF.Pow(x2 - x1, 2) + MathF.Pow(y2 - y1, 2),0.5);

                if (d == 0 && r2 == r1) Console.WriteLine(-1);
                else if (d < r1 + r2 && d > sub) Console.WriteLine(2);
                else if (r1 + r2 == d || sub == d) Console.WriteLine(1);
                else Console.WriteLine(0);
            }
        }
    }
}
