#include <iostream>

int get_digits(const int number);
int sum_odd_digits(const std::string card_number);
int sum_even_digits(const std::string card_numbers);

int main(){

    std::string card_number;
    int results = 0;

    std::cout << "Enter a Credit Card Number: ";
    std::cin >> card_number;

    results = sum_even_digits(card_number) + sum_odd_digits(card_number);

    if(results % 10 == 0){
        std::cout << card_number << " is valid" << '\n';
    }
    else{
        std::cout << card_number << " is not valid" << '\n';
    }

    return 0;
}

int get_digits(const int number){

    return number % 10 + (number/ 10 % 10);
}
int sum_odd_digits(const std::string card_number){
    int sum = 0;

    for(int i = card_number.size() - 2; i >= 0; i-=2){
        sum += get_digits((card_number[i] - '0'));
    }

    return sum;
}
int sum_even_digits(const std::string card_number){

    int sum = 0;

    for(int i = card_number.size() - 2; i >= 0; i-=2){
        sum += get_digits((card_number[i] - '0') * 2);
    }

    return sum;
}