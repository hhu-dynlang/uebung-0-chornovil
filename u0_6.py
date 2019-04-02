def fizz_buzz(n):
    output = list()
    for i in range(1,n):
        if i%3 == 0 and i%5 == 0:
            output.append("fizzbuzz")
        elif i%3 == 0:
            output.append("fizz")
        elif i%5 == 0:
            output.append("buzz")
        else:
            output.append(i)
    return output

print(fizz_buzz(6))
