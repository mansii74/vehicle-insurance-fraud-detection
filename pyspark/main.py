from spark_session import create_spark_session, load_data
from data_analysis import basic_analysis, get_column_types
from feature_engineering import build_feature_pipeline
from fraud_model import train_model
from evaluation import evaluate_model

if __name__ == "__main__":
    spark = create_spark_session()
    df = load_data(spark, "data/raw/carclaims.csv")

    basic_analysis(df)
    num_cols, cat_cols = get_column_types(df)

    df_features = build_feature_pipeline(df, cat_cols, num_cols)
    model, predictions = train_model(df_features)

    evaluate_model(predictions)
