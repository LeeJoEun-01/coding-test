#include <stdio.h>
int main(void)
{
  int num;
  int sum;
  int result = 0;
  scanf("%d\n", &sum);
  scanf("%d\n", &num);

  for (int i = 0; i < num; i++)
  {
    int price;
    int n;
    scanf("%d %d", &price, &n);

    result = result + (price * n);
  }

  if (result == sum)
  {
    printf("Yes\n");
  }
  else
  {
    printf("No\n");
  }
}