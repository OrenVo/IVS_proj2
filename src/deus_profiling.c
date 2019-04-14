/**
* @file deus_profiling.c
* @brief Calculation of the standard deviation of numbers from the inputfile.
*
* @author Pavol Szepsi
*
* @version 1.5.0
* @date 14.4.2019
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
	if (pFile == NULL)
		return 1;

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
	return sqrt(1.0 / (N - 1) * (sumX2 - (N * pow(avgX, 2))));
}

/**
* @brief Main function calling.
*
* @param argc Number of arguments.
* @param argv[] Array of arguments.
*
* @return 0 - Program finished successfully.
* @return 1 - error - File couldn't be opened!
* @return 2 - error - Need filename as the first argument!
* @return 3 - error - Too many arguments!
*/
int main(int argc, char *argv[]) {
	if (argc == 1) {
		fprintf(stderr, "Need filename as the first argument!\n");
		return 2;
	}

	if (argc > 2) {
		fprintf(stderr, "Too many arguments!\n");
		return 3;
	}

	if (StandardDeviation(argv[1]) == 1) {
        fprintf(stderr, "File couldn't be opened!\n");
        return 1;
	}

    printf("%lf\n", StandardDeviation(argv[1]));
	return 0;
}

/**
* @}
*/
