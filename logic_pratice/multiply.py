def multiplication_table(n):
    results = []

    for multiplying in range(1, n + 1):
        memory = []
        for multiplier in range(1, n + 1):
            memory.append(multiplying * multiplier)
        results.append(memory)

    return results

result = multiplication_table(3)

print(result)
