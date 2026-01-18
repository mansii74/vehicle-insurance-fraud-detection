from pyspark.ml.evaluation import MulticlassClassificationEvaluator

def evaluate_model(predictions):
    precision_eval = MulticlassClassificationEvaluator(
        labelCol="FraudFound",
        predictionCol="prediction",
        metricName="weightedPrecision"
    )

    recall_eval = MulticlassClassificationEvaluator(
        labelCol="FraudFound",
        predictionCol="prediction",
        metricName="weightedRecall"
    )

    precision = precision_eval.evaluate(predictions)
    recall = recall_eval.evaluate(predictions)

    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
