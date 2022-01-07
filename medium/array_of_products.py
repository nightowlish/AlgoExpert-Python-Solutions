def arrayOfProducts(array):
    left_products = [1 for element in array]
    right_products = [1 for element in array]
    array_len = len(array)
    for index in range(array_len):
        for i in range(0, index):
            left_products[i] *= array[index]
        for i in range(index + 1, array_len):
            right_products[i] *= array[index]
            
    output = []
    for index in range(array_len):
        output_value = left_products[index] * right_products[index]
        output.append(output_value)
    return output
