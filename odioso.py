odiosos = {i:(bin(i),hex(i)) for i in range(51) if bin(i)[2:].count('1') % 2 != 0}

print odiosos
