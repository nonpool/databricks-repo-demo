

df = spark.read.load('/FileStore/tables/products.csv',
    format='csv',
    header=True
)
display(df.limit(10))