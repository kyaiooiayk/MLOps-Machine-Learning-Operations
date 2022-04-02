import argparse
import pandas as pd
import os

from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn.preprocessing import LabelEncoder

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Read any hyperparameters
    parser.add_argument('--n_clusters', type=int, default=3)

    # Sagemaker specific arguments, use environment values for defaults.
    parser.add_argument('--model_dir', type=str, default=os.environ.get('SM_MODEL_DIR'))
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAIN'))

    args = parser.parse_args()

    # read input file iris_train.csv .
    input_file = os.path.join(args.train, 'iris_train.csv')
    df_iris_train = pd.read_csv(input_file, header=0, engine="python")

    # Convert target variables 'species' from strings into integers.
    labelEncoder = LabelEncoder()
    labelEncoder.fit(df_iris_train['species'])
    df_iris_train['species'] = labelEncoder.transform(df_iris_train['species'])

    # seperate training and validation dataset into seperate features and target variables
    # assume that the first column in each dataset is the target variable.
    # training a k-means classifier does not require labelled data, and therefore
    # df_iris_target_train will not be used.
    df_iris_features_train = df_iris_train.iloc[:,1:]
    df_iris_target_train = df_iris_train.iloc[:,0]

    # create a K-Means multi-class classifier.
    kmeans_model = KMeans(n_clusters=args.n_clusters)
    kmeans_model.fit(df_iris_features_train)

    # save the model.
    joblib.dump(kmeans_model, os.path.join(args.model_dir, "sklearn-kmeans-model.joblib"))


# deserializer.
def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, "sklearn-kmeans-model.joblib"))
    return model