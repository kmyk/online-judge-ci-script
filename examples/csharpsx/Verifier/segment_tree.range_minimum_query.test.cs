using System;
using System.Linq;
using Library;

// verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_A
class range_minimum_query
{
    static void Main()
    {
        var nq = Console.ReadLine().Split().Select(int.Parse).ToArray();
        var (n, q) = (nq[0], nq[1]);
        SegmentTree<int> segTree = new SegmentTree<int>(n, int.MaxValue, Math.Min);

        for (int i = 0; i < q; i++)
        {
            var query = Console.ReadLine().Split().Select(int.Parse).ToArray();
            if (query[0] == 0)
            {
                segTree[query[1]] = query[2];
            }
            else
            {
                Console.WriteLine(segTree[query[1]..(query[2] + 1)]);
            }
        }
    }
}
