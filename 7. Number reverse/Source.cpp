#include <iostream>
#include <cmath>

using namespace std;

int digitsQuantity(int number)
{
	int n = 1;
	while (number / 10 != 0) {
		number /= 10; n++;
	}
	return n;
}

int main()
{
	int number; cin >> number;
	int q = digitsQuantity(number);
	
	int reversed = 0;
	for (int i = 1; i <= q; i++) {
		reversed += (number % int(pow(10, i)) / int(pow(10, i - 1))) * pow(10, q - i);
	}

	cout << reversed;



	system("pause");
	return 0;
}
