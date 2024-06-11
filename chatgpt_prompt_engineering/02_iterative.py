from IPython.display import display, HTML
get_completion = __import__("00_initializing")

# Generating a marketing product description from a product fact sheet.
fact_sheet_chair = """
OVERVIEW
- Part of a beautiful family of mid-century inspired office furniture, 
including filing cabinets, desks, bookcases, meeting tables, and more.
- Several options of shell color and base finishes.
- Available with plastic back and front upholstery (SWC-100) 
or full upholstery (SWC-110) in 10 fabric and 6 leather options.
- Base finish options are: stainless steel, matte black, 
gloss white, or chrome.
- Chair is available with or without armrests.
- Suitable for home or business settings.
- Qualified for contract use.

CONSTRUCTION
- 5-wheel plastic coated aluminum base.
- Pneumatic chair adjust for easy raise/lower action.

DIMENSIONS
- WIDTH 53 CM | 20.87”
- DEPTH 51 CM | 20.08”
- HEIGHT 80 CM | 31.50”
- SEAT HEIGHT 44 CM | 17.32”
- SEAT DEPTH 41 CM | 16.14”

OPTIONS
- Soft or hard-floor caster options.
- Two choices of seat foam densities: 
 medium (1.8 lb/ft3) or high (2.8 lb/ft3)
- Armless or 8 position PU armrests 

MATERIALS
SHELL BASE GLIDER
- Cast Aluminum with modified nylon PA6/PA66 coating.
- Shell thickness: 10 mm.
SEAT
- HD36 foam

COUNTRY OF ORIGIN
- Italy
"""

prompt_1 = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

Technical specifications: ```{fact_sheet_chair}```
"""

print("Prompt1: ", prompt_1)
# response_1 = get_completion(prompt_1)
# print(response_1)

# Issue 1: Text too long
# Use 50 words, 280 characters, 3 sentences and so on.

prompt_2 = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

Use at most 50 words. 

Technical specifications: ```{fact_sheet_chair}```
"""

print("Prompt 2: ", prompt_2)
# response_2 = get_completion(prompt_2)
# print(response_2)

# Issue 2: Text focuses on the wrong details

prompt_3 = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

The description is intended for furniture retailers, 
so should be technical in nature and focus on the 
materials the product is constructed from.

Use at most 50 words.

Technical specifications: ```{fact_sheet_chair}```
"""
print("Prompt 3: ", prompt_3)
# response_3 = get_completion(prompt_3)
# print(response_3)

prompt_4 = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

The description is intended for furniture retailers, 
so should be technical in nature and focus on the 
materials the product is constructed from.

At the end of the description, include every 7-character 
Product ID in the technical specification.

Use at most 50 words.

Technical specifications: ```{fact_sheet_chair}```
"""
print("Prompt 4:\n", prompt_4)
# response_4 = get_completion(prompt_4)
# print(response_4)


# ISSUE 3: Description needs a table of dimensions
prompt_5 = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet. Write a full page HTML/CSS includes styling, css, meta tags and SEO. 

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

The detailed description is intended for furniture retailers, 
so should be technical in nature and focus on the 
materials the product is constructed from.

At the end of the description, include every 7-character 
Product ID in the technical specification.

After the description, include a table that gives the 
product's dimensions. The table should have two columns.
In the first column include the name of the dimension. 
In the second column include the measurements in inches only.

Give the table the title 'Product Dimensions'.

Format everything as HTML that can be used in a website. 
Place the description in a <article> element.
Provide extra information headers like key features, construction, material used and different options in the page

Technical specifications: ```{fact_sheet_chair}```
"""
print("Prompt 5:\n", prompt_5)
# response_5 = get_completion(prompt_5)
# print(response_5)
# display(HTML(response_5))


