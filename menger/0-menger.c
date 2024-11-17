#include "menger.h"

/**
 * menger - Draws a 2D Menger Sponge at a given level
 * @level: Level of the Menger Sponge to draw
 */

void menger(int level)
{
	int n, m, j, x, y;
	char s;

	m = pow(3, level);
	for (n = 0; n < m; n++)
	{
		for (j = 0; j < m;)
		{
			s = '#';
			x = n;
			y = j++;
			while (x > 0 || y > 0)
			{
				if (x % 3 == 1 && y % 3 == 1)
				{
					s = ' ';
				}
				x /= 3;
				y /= 3;
			}
			printf("%c", s);
		}
		printf("\n");
	}
}