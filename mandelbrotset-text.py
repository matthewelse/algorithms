for y in range(0, 100):
    output = ""
    for x in range(0, 100):
        c = (3.5*(float(x)/100) - 2.5) + (2*(float(y)/100) - 1)*1j
        z = 0.0 + 0.0j

        iterations = 0
    
        while (z.real**2 + z.imag**2 < 4 and iterations < 50):
            z = (z**2 + c)
            iterations += 1

        if iterations == 50:
            output += "*"
        else:
            output += " "
    print output
