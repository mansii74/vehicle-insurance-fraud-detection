from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml import Pipeline

def build_feature_pipeline(df, categorical_cols, numerical_cols):
    indexers = [
        StringIndexer(inputCol=col, outputCol=f"{col}_indexed", handleInvalid="keep")
        for col in categorical_cols
    ]

    feature_cols = [f"{col}_indexed" for col in categorical_cols] + numerical_cols

    assembler = VectorAssembler(
        inputCols=feature_cols,
        outputCol="features"
    )

    pipeline = Pipeline(stages=indexers + [assembler])
    model = pipeline.fit(df)

    transformed_df = model.transform(df)
    return transformed_df
