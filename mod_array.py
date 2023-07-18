# def get_mod_array(num_array: list, divisor: int) -> int:
#     num = ""
#     for x in num_array:
#         num += str(x)
#     number = int(num)
#     return number % divisor


def get_mod_array(num_array: list, divisor: int) -> int:
    power, result = 1, 0
    for val in range(len(num_array) - 1, -1, -1):
        result = (result + ((num_array[val] % divisor) * power)) % divisor
        power = (power * 10) % divisor

    return result


try:
    nums_array = list(map(int, input("Enter integers separated by space : ").split()))
    divisor = int(input("Enter divisor : "))
    print("Therefore, the mod array value is : ", get_mod_array(nums_array, divisor))
except ValueError:
    print("Invalid Input. Please Enter only integers")