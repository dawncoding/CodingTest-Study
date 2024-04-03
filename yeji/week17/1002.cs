using System;
using System.Collections.Generic;
using System.Text;

namespace baek2
{
    class Program
    {
        public static void Main()
        {
            string input = Console.ReadLine();
            int answer = 0;
            Stack<char> stack = new Stack<char>();
            for(int i = 0; i<input.Length;i++)
            {
                if (input[i] == '(')
                    stack.Push(input[i]);
                else // ')'인 경우
                {
                    stack.Pop();
                    if (input[i-1] == '(') // 레이저인 경우
                        answer += stack.Count;

                    else // 끝인 경우
                        answer++;
                }
            }
            Console.Write(answer);
             
        }
    }
}
