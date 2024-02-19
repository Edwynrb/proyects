print("A toy store is very successful in two of its products: clowns and dolls. They usually sell by mail and the logistics company charges them by weight of each package, so they must calculate the weight of the clowns and dolls that will appear in each package on demand. Each clown weighs 112 g and each doll 75 g. Write a program that reads the number of clowns and dolls sold in the last order and calculates the total weight of the package that will be shipped.")
CLOWNS_WEIGHT = 112
DOLLS_WEIGHT = 75
clowns_numbers = int(input("Enter numbers of clowns for package "))
dolls_numbers = int(input("Enters numbers of dolls for package "))
package_weight = (clowns_numbers *CLOWNS_WEIGHT) + (dolls_numbers * DOLLS_WEIGHT)
print(f"The total weight of the package is {package_weight}") 