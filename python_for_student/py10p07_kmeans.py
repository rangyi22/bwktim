#py10p07_kmeans.py
# > pip install sklearn # Windows PowerShell에서 sklearn을 설치해야
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {'x': [50,68,44,54,66,66,62,44,70,68,134,108,114,86,100,
              114,118,104,130,94,98,96,70,66,88,90,76,86,102,92],
        'y': [79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,
              36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]
       }
df = pd.DataFrame(data)
Nclusters = [2, 3] # cluster 개수
colors = ['red', 'green','blue', 'yellow'] # cluster별 색깔들
for i,Ncluster in enumerate(Nclusters):
   plt.subplot(2,3,i+1)
   kmeans = KMeans(n_clusters=Ncluster).fit(df)
   centroids = kmeans.cluster_centers_
   for n,centroid in enumerate(centroids): #각 cluster의 controid
      print(f'{n}({colors[n]:6s}):', centroid) 
   print("\nCluster labels for each sample=\n", kmeans.labels_)
   cs = [colors[label] for label in kmeans.labels_]
   plt.scatter(df['x'], df['y'], c=cs, s=5, alpha=0.5)
   plt.scatter(centroids[:,0], centroids[:,1], 
               c=colors[:Ncluster], s=20)
plt.show()
