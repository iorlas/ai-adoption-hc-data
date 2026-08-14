# Databricks notebook source
# MAGIC %md
# MAGIC # Donor profiling
# MAGIC
# MAGIC Profiles the `donor` table: null counts, distinct counts, and a bit of
# MAGIC standardisation. This notebook is written the way profiling notebooks
# MAGIC often grow in real life — by copy-pasting the same block for each column.
# MAGIC The repetition is deliberate: on Day 3 you will cluster these near-
# MAGIC duplicate cells and draft a small reusable module.
# MAGIC
# MAGIC Set `CATALOG` and `SCHEMA` to your own training schema before running.

# COMMAND ----------

CATALOG = "training"
SCHEMA = "your_schema"   # <-- change to your own schema
donor = spark.read.table(f"{CATALOG}.{SCHEMA}.donor")
donor.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Null counts, column by column (copy-pasted per column)

# COMMAND ----------

from pyspark.sql import functions as F

# email
n_total = donor.count()
n_null = donor.filter(F.col("email").isNull()).count()
print("email", "nulls:", n_null, "pct:", round(100.0 * n_null / n_total, 1))

# COMMAND ----------

# phone
n_total = donor.count()
n_null = donor.filter(F.col("phone").isNull()).count()
print("phone", "nulls:", n_null, "pct:", round(100.0 * n_null / n_total, 1))

# COMMAND ----------

# postcode
n_total = donor.count()
n_null = donor.filter(F.col("postcode").isNull()).count()
print("postcode", "nulls:", n_null, "pct:", round(100.0 * n_null / n_total, 1))

# COMMAND ----------

# nhs_number
n_total = donor.count()
n_null = donor.filter(F.col("nhs_number").isNull()).count()
print("nhs_number", "nulls:", n_null, "pct:", round(100.0 * n_null / n_total, 1))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Distinct counts (again, one block per column)

# COMMAND ----------

# status distinct values
donor.groupBy("status").count().orderBy(F.desc("count")).show(truncate=False)

# COMMAND ----------

# ethnicity distinct values
donor.groupBy("ethnicity").count().orderBy(F.desc("count")).show(truncate=False)

# COMMAND ----------

# sex distinct values
donor.groupBy("sex").count().orderBy(F.desc("count")).show(truncate=False)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Standardise text columns (same trim/collapse pattern each time)

# COMMAND ----------

# standardise postcode: upper, strip, collapse inner spaces
donor = donor.withColumn(
    "postcode_clean",
    F.upper(F.regexp_replace(F.trim(F.col("postcode")), r"\s+", " ")),
)

# COMMAND ----------

# standardise status: initcap, strip
donor = donor.withColumn(
    "status_clean",
    F.initcap(F.trim(F.col("status"))),
)

# COMMAND ----------

# standardise ethnicity: strip, collapse spaces
donor = donor.withColumn(
    "ethnicity_clean",
    F.regexp_replace(F.trim(F.col("ethnicity")), r"\s+", " "),
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Age at registration (business rule check: should be 16-30)

# COMMAND ----------

donor = donor.withColumn(
    "age_at_registration",
    F.floor(F.datediff(F.col("registered_date"), F.col("date_of_birth")) / 365.25),
)
donor.filter((F.col("age_at_registration") < 16) | (F.col("age_at_registration") > 30)) \
     .select("donor_id", "registry_id", "age_at_registration").show()

# COMMAND ----------

display(donor)
