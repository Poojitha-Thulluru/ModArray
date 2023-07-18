def get_mod_array(num_array: list, divisor: int) -> int:
    num = ""
    for x in num_array:
        num += str(x)
    number = int(num)
    return number % divisor


try:
    nums_array = list(map(int, input("Enter integers separated by space : ").split()))
    divisor = int(input("Enter divisor : "))
    print("Therefore, the mod array value is : ", get_mod_array(nums_array, divisor))
except ValueError:
    print("Invalid Input. Please Enter only integers")