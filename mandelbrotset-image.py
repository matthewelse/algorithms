from PIL import Image

w = 5000
h = 1000

max_iterations = 100

colours = [(162,143,130),(164,140,129),(167,137,127),(169,135,126),(171,132,125),(174,129,123),(176,126,122),(179,123,121),(181,121,119),(183,118,118),(186,115,117),(188,112,115),(190,109,114),(193,107,113),(195,104,112),(197,101,110),(200,98,109),(202,95,108),(204,93,106),(207,90,105),(209,87,104),(212,84,102),(214,81,101),(216,79,100),(221,73,97),(215,74,97),(210,74,97),(204,75,97),(198,76,97),(193,76,97),(187,77,97),(182,77,96),(176,78,96),(170,79,96),(165,79,96),(159,80,96),(153,81,96),(148,81,96),(142,82,96),(136,83,96),(131,83,96),(125,84,96),(119,85,96),(114,85,95),(108,86,95),(103,86,95),(97,87,95),(91,88,95),(86,88,95),(80,89,95),(84,94,98),(89,99,100),(93,103,103),(98,108,105),(102,113,108),(106,118,110),(111,123,113),(115,127,115),(120,132,118),(124,137,121),(128,142,123),(133,147,126),(137,151,128),(142,156,131),(146,161,133),(150,166,136),(155,171,139),(159,175,141),(164,180,144),(168,185,146),(172,190,149),(177,195,151),(181,199,154),(186,204,156),(190,209,159),(191,209,157),(193,210,156),(194,210,154),(196,211,152),(197,211,151),(198,212,149),(200,212,148),(201,213,146),(203,213,144),(204,213,143),(205,214,141),(207,214,139),(208,215,138),(210,215,136),(211,216,134),(212,216,133),(214,216,131),(215,217,129),(217,217,128),(218,218,126),(219,218,125),(221,219,123),(222,219,121),(224,220,120),(225,220,118)]

img = Image.new("RGB", (w, h), "white")
pixels = img.load()

try:
    for y in range(0, h):
        output = ""
        for x in range(0, w):
            c = (3.5*(float(x)/w) - 2.5) + (2*(float(y)/h) - 1)*1j
            z = 0.0 + 0.0j

            iterations = 0
            while (z.real**2 + z.imag**2 < 4 and iterations < max_iterations):
                z = (z**2 + c)
                iterations += 1

            pixels[x, y] = colours[iterations-1]
except (KeyboardInterrupt):
    img.save("mandelbrot.png", "PNG")
img.save("mandelbrot.png", "PNG")
