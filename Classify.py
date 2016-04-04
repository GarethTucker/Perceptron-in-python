import random


class Classify (object):
    def __init__(self, data):
        images = data.images
        instance_classes = data.instance_classes
        # print('INSTANCE CLASSES: ')
        # print(instance_classes)
        features = self.construct_features()
        feature_values = self.get_feature_values(images, features)
        # print('FEATURE VALUES')
        # for feature_value in feature_values:
        #     print(feature_value)
        self.LEARNING_RATE = 100
        MAX_RUNS = 1000
        weights = self.initialise_weights(0.0, 0.5)
        print('Starting Weights: ')
        twodecimals = ["%.2f" % v for v in weights]
        print(", ".join(twodecimals))
        # print('feature_values len: %d'%len(feature_values))
        # print('images len: %d'%len(images))
        self.perceptron_call = 0
        perceptron_correct = False
        runs = 0
        while perceptron_correct == False and runs < MAX_RUNS:
            perceptron_correct = self.perceptron(weights, images, feature_values, instance_classes)
            runs += 1
        if perceptron_correct:
            print('Perceptron is classifying all images correctly')
            print('It took %d runs'%runs)
        else:
            print("Perceptron did not correctly classify all images correctly within MAX_RUNS limit")
            print('Ran %d times'%MAX_RUNS)
        print('Final Weights: ')
        twodecimals = ["%.2f" % v for v in weights]
        print(", ".join(twodecimals))

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

    def get_sum_of_features_times_weights(self, weights, feature_values):
        # print('feature_values in sum method')
        # print(feature_values)
        sum = 0.0
        for index in range (0, len(weights)):
            weight = weights[index]
            # print('weight: %f'%weight)
            feature_value = feature_values[index]
            # print('feature_value: %d'%feature_value)
            weighted_feature = float(weight*feature_value)
            sum += weighted_feature
        # print('sum: %f'%sum)
        return sum

    def perceptron(self, weights, images, feature_values, instance_classes):
        self.perceptron_call += 1
        # print('perceptron_call: %d'%self.perceptron_call)
        # print('weights: ')
        # print(weights)
        # print('weights length: %d'%len(weights))
        # print('feature values:')
        # print(feature_values)
        # print('feature_values length: %d'%len(feature_values))
        # print('instance_class: ')
        # print(instance_classes)
        all_images_correctly_classified = True
        for image_index in range(0, len(images)):
            # for row in images[index]:
            #     print(row)
            features = feature_values[image_index]
            sum_of_features_times_weights = self.get_sum_of_features_times_weights(weights, features)

            # print('sum_of_features_times_weights : %f'%sum_of_features_times_weights )
            # print('instance_class: %d'%instance_classes[image_index])
            if instance_classes[image_index] > 0 and sum_of_features_times_weights <= 0:
                # print('positive instance classified as negative, increasing weights')
                for weight_index in range(0, len(weights)):
                    weight = weights[weight_index]
                    feature = features[weight_index]
                    new_weight = weight + (feature*self.LEARNING_RATE)
                    weights[weight_index] = new_weight
                    all_images_correctly_classified = False
            if instance_classes[image_index] < 0 and sum_of_features_times_weights > 0:
                # print('negative instance classified as positive, lowering weights')
                for weight_index in range(0, len(weights)):
                    weight = weights[weight_index]
                    feature = features[weight_index]
                    new_weight = weight - (feature*self.LEARNING_RATE)
                    weights[weight_index] = new_weight
                    all_images_correctly_classified = False
            # print('\n')
        return all_images_correctly_classified