import barcode
from barcode.writer import ImageWriter

# List of missing numbers
missing_numbers = [
    "000002", "000004", "000005", "000007", "000009", "000010", "000011", "000012", "000013",
    "000014", "000015", "000016", "000017", "000019", "000020", "000021", "000028", "000030",
    "000031", "000032", "000035", "000037", "000038", "000040", "000043", "000052", "000054",
    "000055", "000056", "000057", "000058", "000059", "000060", "000061", "000062", "000063",
    "000064", "000065", "000066", "000067", "000068", "000069", "000070", "000071", "000072",
    "000073", "000074", "000075", "000076", "000077", "000078", "000079", "000080", "000081",
    "000082", "000083", "000084", "000085", "000086", "000087", "000088", "000089", "000090",
    "000091", "000092", "000093", "000094", "000095", "000096", "000097", "000098", "000099", "000100"
]

# Function to generate barcodes
def generate_barcodes(numbers):
    for number in numbers:
        # Generate Code128 barcode with ImageWriter
        code128 = barcode.get('code128', number, writer=ImageWriter())
        
        # Customize the writer options to make the barcode wider
        options = {
            'module_width': 0.5,  # Increase module width for a wider barcode
            'module_height': 15,  # Set module height
            'font_size': 10,      # Set font size
            'text_distance': 5.0  # Set distance between the barcode and the text
        }
        
        # Save barcode as an image file
        filename = f'barcode_{number}'
        code128.save(filename, options=options)

# Generate the barcodes for the missing numbers
generate_barcodes(missing_numbers)

print("Barcodes generated successfully.")
