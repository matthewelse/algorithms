#include <stdio.h>
#include <stdlib.h>

int binary_search(int, int[], int, int, int);

int main(void) {
	int numbers[] = {1,2,3,4,5,6,7,8,9,10,15};
	int size = sizeof(numbers)/sizeof(int);
	
	int search;
	
	printf("Enter search term... \n");
	scanf("%d", &search);
	
	printf("Searching for: %i\n", search);
	
	printf("Output: %i\n", binary_search(search, numbers, size, 0, size-1));
	
	return 0;
}

int binary_search(int find, int list[], int size, int start, int end) {
	if (size == 1) {
		if (find == list[0])
			return start;
		else
			return -1;
	}
	
	// Split the array in half
	int centre = size / 2;
	
	if (abs(list[centre-1] - find) < abs(list[centre] - find)) {
		int numbers[centre];
		
		int x = 0;
		for (; x < centre; x++)
			numbers[x] = list[x];
			
		return binary_search(find, numbers, centre,start,start+centre);
	}
	else {
		int numbers[size - centre + 1];
		
		int x = 0;
		for (; x < size - centre; x++)
			numbers[x] = list[x+centre];
		
		return binary_search(find, numbers, size-centre, start+centre, end);
	}
	
}
