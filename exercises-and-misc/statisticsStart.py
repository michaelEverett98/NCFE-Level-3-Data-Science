# 1. Import libraries
import pandas as pd
from fuzzywuzzy import process

# ----------------------------
# 2. Create sample datasets
# ----------------------------

# Internal dataset: sales transactions
sales = pd.DataFrame({
    "CustomerID": [101, 102, 103, 104],
    "Product": ["Laptop", "Tablet", "Phone", "Laptop"],
    "Amount": [1200, 300, 600, 1300],
    "Date": ["2025-09-01", "2025-09-02", "2025-09-02", "2025-09-03"]
})

# External dataset: customer demographics (Excel / CRM export)
customers = pd.DataFrame({
    "CustomerID": [101, 102, 103, 104],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [34, 45, 29, 40],
    "Region": ["London", "Manchester", "London", "Birmingham"]
})

# Open dataset: regional population (government dataset)
population = pd.DataFrame({
    "Region": ["London", "Manchester", "Birmingham"],
    "Population": [9500000, 2800000, 1150000]
})

# Create prouct_categories
product_categories = pd.DataFrame({
    "ProductID": [1, 2, 3],
    "ProductType": ["Communication", "Entertainment", "Work"],
    "Product": ["Phone", "Tablet", "Laptop"],
    "Brand": ["Apple", "Samsung", "Windows"]
})
print("Sales Dataset:\n", sales, "\n")
print("Customer Dataset:\n", customers, "\n")
print("Population Dataset:\n", population, "\n")
print("Product Dataset:\n", product_categories, "\n")

# ----------------------------
# 3. Blend datasets
# ----------------------------

# Step 3.1: Merge Sales + Customer demographics on CustomerID
sales_customers = pd.merge(sales, customers, on="CustomerID", how="inner")

# Step 3.2: Add population data (Join on Region)
blended_data = pd.merge(sales_customers, population, on="Region", how="left")
print("Blended Dataset:\n", blended_data, "\n")

# ----------------------------
# 4. Example of Fuzzy Matching
# ----------------------------

# Suppose Region names are inconsistent
population_alt = pd.DataFrame({
    "Region": ["London City", "Manchesterr", "Birmnghm"],
    "Population": [9500000, 2800000, 1150000]
})

# Fuzzy match function
def fuzzy_match(value, choices, scorer="ratio"): # The scorer = "ratio" parameter exists in order to specify the keyword/method which the extractOne should use
    match, score = process.extractOne(value, choices)
    return match if score > 80 else None

# Map corrected regions
population_alt["Region_Corrected"] = population_alt["Region"].apply(
    lambda x: fuzzy_match(x, blended_data["Region"].unique())
)
print("Fuzzy Matched Population Data:\n", population_alt, "\n")

# ----------------------------
# 5. Save blended dataset
# ----------------------------
blended_data.to_csv("blended_dataset.csv", index=False)
print(" Blended dataset saved as blended_dataset.csv\n")

# Inner join sales + customers on CustomerID
inner_joined = pd.merge(sales, customers, on="CustomerID", how="inner")
print("Inner Join:\n", inner_joined, "\n")

# Full outer join sales + population on Region
full_joined = pd.merge(
    pd.merge(sales, customers, on="CustomerID", how="inner"),
    population,
    on="Region",
    how="outer"
)
print("Full Outer Join:\n", full_joined, "\n")

# Left join blended_data + product_categories on Product
left_joined = pd.merge(blended_data, product_categories, on="Product", how="left")
print("Left Join:\n", left_joined, "\n")

# Right join blended_data + product_categories on Product
right_joined = pd.merge(blended_data, product_categories, on="Product", how="right")
print("Right Join:\n", right_joined, "\n")

# Union of two sales datasets (imagine a new sales month)
sales_new = pd.DataFrame({
    "CustomerID": [105, 106],
    "Product": ["Phone", "Tablet"],
    "Amount": [700, 400],
    "Date": ["2025-09-04", "2025-09-05"]
})
union_joined = pd.concat([sales, sales_new], 
ignore_index=True)
print("Union Join (Concat):\n", union_joined, "\n")