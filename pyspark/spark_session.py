from pyspark.sql import SparkSession

def create_spark_session():
    spark = SparkSession.builder \
        .appName("VehicleInsuranceFraudDetection") \
        .getOrCreate()
    return spark

def load_data(spark, file_path):
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    return df

if __name__ == "__main__":
    spark = create_spark_session()
    df = load_data(spark, "data/raw/carclaims.csv")
    df.show(5)
    df.printSchema()
