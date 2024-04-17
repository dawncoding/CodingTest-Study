using System.Collections.Generic;
using System;

class Solution
{
    public static void turn(ref List<string> list, int dir)
    {
        if (dir == -1)
        {
            string first = list[0];
            list.RemoveAt(0);
            list.Add(first);
        }
        else
        {
            string last = list[list.Count - 1];
            list.RemoveAt(list.Count - 1);
            list.Insert(0, last);
        }
    }

    public static bool check(List<string> left,List<string> right)
    {
        return left[2] != right[right.Count - 2];
    }
    public static void Main(string[] args)
    {
        string list1_array = Console.ReadLine();
        string list2_array = Console.ReadLine();
        string list3_array = Console.ReadLine();
        string list4_array = Console.ReadLine();

        List<string> list1 = new List<string>();
        List<string> list2 = new List<string>();
        List<string> list3 = new List<string>();
        List<string> list4 = new List<string>();
        for (int i = 0; i < 8; i++)
        {
            list1.Add(list1_array[i].ToString());
            list2.Add(list2_array[i].ToString());
            list3.Add(list3_array[i].ToString());
            list4.Add(list4_array[i].ToString());
        }

        int n = int.Parse(Console.ReadLine());

        while (n > 0)
        {
            n--;
            int[] input = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int num = input[0];
            int dir = input[1];

            switch (num)
            {
                case 1:
                    if (check(list1, list2))
                    {
                        if (check(list2, list3))
                        {
                            if (check(list3, list4)) turn(ref list4, -dir);
                            turn(ref list3, dir);
                        }
                        turn(ref list2, -dir);
                    }
                    turn(ref list1, dir);
                    break;
                case 2:
                    if (check(list2, list3))
                    {
                        if (check(list3, list4)) turn(ref list4, dir);
                        turn(ref list3, -dir);
                    }
                    if (check(list1, list2)) turn(ref list1, -dir);
                    turn(ref list2, dir);
                    break;
                case 3:
                    if (check(list2, list3))
                    {
                        if (check(list1, list2)) turn(ref list1, dir);
                        turn(ref list2, -dir);
                    }
                    if (check(list3, list4)) turn(ref list4, -dir);
                    turn(ref list3, dir);
                    break;
                case 4:
                    if (check(list3, list4))
                    {
                        if (check(list2, list3))
                        {
                            if (check(list1, list2)) turn(ref list1, -dir);
                            turn(ref list2, dir);
                        }
                        turn(ref list3, -dir);
                    }
                    turn(ref list4, dir);
                    break;
            }
        }
        int answer = 0;
        answer += int.Parse(list1[0]) == 0 ? 0 : 1;
        answer += int.Parse(list2[0]) == 0 ? 0 : 2;
        answer += int.Parse(list3[0]) == 0 ? 0 : 4;
        answer += int.Parse(list4[0]) == 0 ? 0 : 8;

        Console.Write(answer);
    }
}
