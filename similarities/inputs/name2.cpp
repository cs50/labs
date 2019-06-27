#include <string>
#include <iostream>

int main()
{
  std::string name;
  std::cout << "What's your name? ";
  getline (std::cin, name);
  std::cout << "Hi, " << name << "!\n";
}
