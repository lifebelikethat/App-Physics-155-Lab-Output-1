# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the larges palindrome made from the product of two 3-digit numbers.

products = []
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        str_product = str(product)
        product_length = len(str_product)
        if len(str_product) % 2 == 0:
            first_half = str_product[0:int(product_length/2)]
            second_half = str_product[-1:int(product_length/2)-1:-1]
            if first_half == second_half:
                products.append(product)

        elif len(str_product) % 2 != 0:
            first_half = str_product[0:len(str_product)//2]
            second_half = str_product[-1:len(str_product)//2:-1]

            if int(first_half) == int(second_half):
                products.append(product)

print(max(products))

