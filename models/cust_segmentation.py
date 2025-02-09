from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import pickle, logging

def label_clusters(row):
    if row["cluster"] == 0:
        return "Yeni Müşteriler"
    elif row["cluster"] == 1:
        return "Sadık Müşteriler"
    elif row["cluster"] == 2:
        return "Potansiyel Churn"
    elif row["cluster"] == 3:
        return "Churn Müşteriler"
    else:
        return "Potansiyel Müşteriler"

def save_model(model, model_filename='assets/kmeans_model.pkl'):
    logging.info(f"Saving model to {model_filename}...")
    try:
        with open(model_filename, 'wb') as model_file:
            pickle.dump(model, model_file)
        logging.info(f"Model saved successfully to {model_filename}.")
    except Exception as e:
        logging.error(f"Error saving model: {e}")

def predict_data(data):
    logging.info("Starting model prediction process...")
    scaler = StandardScaler()
    try:
        df = data.drop(columns=['cb_customer_id', 'first_transaction', 'last_transaction', 'total_spent'])
        df_scaled = scaler.fit_transform(df)
        logging.info("Data scaling completed.")

        optimal_k = 5 
        kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
        df["cluster"] = kmeans.fit_predict(df_scaled)
        logging.info("KMeans clustering completed.")

        df["Segment"] = df.apply(label_clusters, axis=1)
        logging.info("Segmentation labels added to data.")

        save_model(kmeans)
        
        return df
    except Exception as e:
        logging.error(f"Error during prediction process: {e}")
        raise

