from pyspark.ml.classification import DecisionTreeClassifier

def train_model(df):
    dt = DecisionTreeClassifier(
        labelCol="FraudFound",
        featuresCol="features",
        maxDepth=5
    )

    model = dt.fit(df)
    predictions = model.transform(df)
    return model, predictions
