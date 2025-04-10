import cv2
import numpy as np
from sklearn.cluster import KMeans

def extract_key_colors(image, n_colors=5):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = img.reshape(-1, 3)
    kmeans = KMeans(n_clusters=n_colors).fit(img)
    centers = kmeans.cluster_centers_.astype('uint8')
    labels = kmeans.labels_
    return centers, labels

def simulate_protanopia(color):
    r, g, b = color
    return [r * 0.56667 + g * 0.43333, r * 0.55833 + g * 0.44167, b]

def recolor_image(image):
    centers, labels = extract_key_colors(image)
    new_centers = np.array([simulate_protanopia(c) for c in centers]).astype('uint8')
    recolored = new_centers[labels]
    recolored_image = recolored.reshape(image.shape)
    return recolored_image




