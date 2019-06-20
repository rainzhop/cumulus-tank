// int binsearch(int x, int v[], int n)
// {
// 	int low, high, mid;

// 	low = 0;
// 	high = n - 1;
// 	while (low <= high)
// 	{
// 	    mid = (low + high) / 2;
// 	    if (x < v[mid])
// 	        high = mid - 1;
// 	    else if (x > v[mid])
// 	        low = mid + 1;
// 	    else /* found match */
// 	        return mid;
// 	}
// 	return -1; /* no match */
// }

/*
 * 在上面有关折半查找的例子中，while循环语句内共执行了两次测试，
 * 其实只要一次就足够（代价是将更多的测试在循环外执行）。
 * 重写该函数，使得在循环内部只执行一次测试。
 */

int binsearch_new(int x, int v[], int n)
{
    int low, high, mid;
    
    low = 0;
    high = n - 1;
    while (low < high)
    {
        mid = (low + high) / 2;
        if (x <= v[mid])
            high = mid;
        else
            low = mid + 1;
    }
    
    return (x == v[low]) ? low : -1;
}
