from pylibdmtx.pylibdmtx import decode
import cv2


image = cv2.imread("image2.jpg", cv2.IMREAD_GRAYSCALE) 


decoded = decode(image)

for obj in decoded:
    data = obj.data.decode("utf-8")
    print("Decoded information:", data)


output_file = "decoded_datamatrix.png"
cv2.imwrite(output_file, image)
print(f" Image saved as {output_file}")

cv2.imshow("Barcode", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
