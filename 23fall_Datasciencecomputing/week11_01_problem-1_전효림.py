import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.colors as mcolors
# %matplotlib inline

class Kmeans:
    def __init__(self, data, k=3, max_iter = None, threshold=1e-6):
        self.data = data # Your Code Here
        self.k = k # Your Code Here
        self.max_iter = max_iter if max_iter is not None else 10 # Your Code Here
        self.threshold = threshold # Your Code Here
        self.colors = ListedColormap(['#D98683', '#7A95E6', '#7B1B86'])#'blue', 'purple', 'red', 'yellow']) # Your Code Here 
        self.centroids = []# Your Code Here

    def show(self):
        ### Edit Here ###

        if len(self.centroids) !=0:
            #######
            fig, ax = plt.subplots()
            colors = self.colors(np.arange(self.k))
            for cluster in range(self.k):
                cluster_data = self.data[self.data['centroid'] == cluster]
                ax.scatter(cluster_data['x'], cluster_data['y'], c=colors[cluster], label=f'Cluster {cluster}')
            
            centroid_colors = self.colors.colors 
            for i in range(self.k):
                ax.scatter(self.centroids['x'][i], self.centroids['y'][i], c=centroid_colors[i], marker="^", s= 100,  label='Centroids')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.show()
 
        else:
            plt.scatter(self.data['x'], self.data['y'], c='#4B76AF', marker='o')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.show()

        ##################

    def distance(self, d1, d2):
        ### Edit Here ###
        # Calculate the distance
        dis = np.sqrt((d1['x'] - d2['x']) ** 2 + (d1['y'] - d2['y']) ** 2)
        return dis

        ##################

    def assign_centroid(self):
        ### Edit Here ###
        # Assign each data point to nearest centroid
        for idx, point in self.data.iterrows():
            distances = [self.distance(point, centroid) for idx, centroid in self.centroids.iterrows()]
            min_distance_idx = np.argmin(distances)
            self.data.at[idx, 'centroid'] = min_distance_idx

        ##################

    def update(self):
        ### Edit Here ###
        # Update centroids
        self.centroids = self.data.sample(self.k)[['x', 'y']].values # 초기화
        self.centroids = pd.DataFrame(self.centroids, columns = ['x', 'y'])
        
        for _ in range(self.max_iter):
            prev_centroids = self.centroids.copy()
            #print(prev_centroids.shape)
            self.assign_centroid()

            for i in range(self.k):
                cluster_points = self.data[self.data['centroid'] == i][['x', 'y']]
                if len(cluster_points) > 0:
                    self.centroids[i] = cluster_points.mean()


            if self.centroids.shape != (3,2):
                self.centroids = self.centroids[['x', 'y']]

            if np.all(np.abs(prev_centroids - self.centroids) < self.threshold):
                break

        ##################

if __name__ == '__main__':
    data = pd.read_csv('C:/Users/wjsgy/OneDrive/바탕 화면/데사컴/W11/dataset-2.csv')
    kmeans = Kmeans(data)
    kmeans.show() # cluster 부여 전 데이터 시각화

    kmeans.update()
    kmeans.show() # cluster 부여 후 cluster별 색상 부여 및 데이터와 centroid 시각화



