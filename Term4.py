import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

df= pd.read_csv('Live.csv')

df.shape

df.head()

df.info()

df.isnull().sum()

df.drop(['Column1','Column2','Column3','Column4'], axis=1, inplace=True)

df.info()

df.describe()

df['status_id'].unique()

len(df['status_id'].unique())

df['status_published'].unique()

len(df['status_published'].unique())

df['status_type'].unique()

len(df['status_type'].unique())

df.drop(['status_id','status_published'],axis=1, inplace=True)

df.info()

df.head()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['status_type']=le.fit_transform(df['status_type'])

df.info()

df.head()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(df)

kmeans.cluster_centers_

kmeans.labels_

df['cluster']=kmeans.labels_

sns.lmplot('status_type','num_wows',data=df, hue='cluster', palette='coolwarm', size=4, aspect=1, fit_reg=False)

