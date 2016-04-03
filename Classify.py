import random
class Classify (object):
    def __init__(self, data):
        images = data.images
        features = self.construct_features()
        feature_values = self.get_feature_values(images, features)
        self.LEARNING_RATE = 0.025
        weights = self.initialise_weights(0.0, 0.5)
        weights = self.perceptron(weights, images, feature_values[0])

    def construct_features(self):
        features = []
        for i in range(0, 50):
            feature = []
            for j in range (0, 4):
                row = random.randint(0,9)
                col = random.randint(0,9)
                sgn = random.randint(0,1)
                pixel = [row, col, sgn]
                feature.append(pixel)
            features.append(feature)
        return features

    def get_feature_values(self, images, features):
        feature_values = []
        for image in images:
            feature_value = self.get_feature_value(image, features)
            feature_value.append(1)
            feature_values.append(feature_value)
        return feature_values

    def get_feature_value(self, image, features):
        feature_value = []
        for feature in features:
            sum = 0
            for pixel in feature:
                row = pixel[0]
                col = pixel[1]
                sgn = pixel[2]
                if image[row][col] == str(sgn):
                    sum += 1
            feature_value.append(1 if sum >= 3 else 0)
        return feature_value

    def initialise_weights(self, start, end):
        weights = []
        for i in range(0, 51):
            weight = random.uniform(start, end)
            weights.append(weight)
        return weights

    def perceptron(self, weights, images, feature_values):
        print('weights length: %d'%len(weights))
        print('feature_values length: %d'%len(feature_values))
        image = images[0]
        for row in image:
            print(row)
        # for feature in feature_values:

