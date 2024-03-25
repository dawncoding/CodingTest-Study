using System;

namespace baek2
{
    class Program
    {
        public static void Main()
        {
            int[] input = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int n = input[0];
            int r = input[1];
            int c = input[2];
            int half = 0;
            int size = 0;
            int answer = 0;
            while(n>0)
            {
                half = (int)Math.Pow(2, n - 1);
                size = half * half; // 한 구역의 크기
                
                if (r < half && c >= half) // 2사분면
                {
                    c -= half;
                    answer += size ;
                }
                else if (r >= half && c<half) //3사분면
                {
                    r -= half;
                    answer += size * 2;
                }
                else if (r >= half && c >= half) //4사분면
                {
                    c -= half;
                    r -= half;
                    answer += size * 3;
                }
                n--;

            }
            Console.Write(answer);
        }
    }
}
