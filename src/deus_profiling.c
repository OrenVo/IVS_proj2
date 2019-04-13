/**
* @file deus_profiling.c
*
* @author Pavol Szepsi
*
* @date 13.4.2019
*/

# include <stdio.h>
# include <math.h>

/**
* @brief Function calculates standard deviation.
*
* @param file Input file with numbers.
*
* @return Standard deviation of numbers from input.
*/
double StandardDeviation(char *file) {
	
	FILE *pFile;
	pFile = fopen(file, "r");
	if (pFile == NULL) {
		printf("Subor sa nepodarilo otvorit.\n");
		return 1;
	}

	double x, avgX;
	double sumX = 0;
	double sumX2 = 0;
	int N = 0;

	while (fscanf(pFile, "%lf", &x) != EOF) {
		sumX += x;
		sumX2 += pow(x, 2);
		N += 1;
	}

	fclose(pFile);

	avgX = sumX / N;
	double y = (double)1 / (N - 1);
	double s = sqrt(y * (sumX2 - (N * pow(avgX, 2))));
	return s;
}

int main(int argc, char *argv[])
{
	if (argc == 1) {
		printf("Prvy argument musi byt nazov suboru.\n");
		return 1;
	}
	if (argc > 2) {
		printf("Prilis vela argumentov.\n");
		return 1;
	}
	printf("%lf\n", StandardDeviation(argv[1]));
	return 0;
}

/**
 * @}
 */