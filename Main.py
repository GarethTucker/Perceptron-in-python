

class Main (object):
    def __init__(self, perceptron_file):
        self.images = list()
        with open (perceptron_file) as f:
            lines = f.readlines()
            line_number = 0;
            while line_number < len(lines):
                if len(lines[line_number]) > 10:
                    line = lines[line_number] + lines[line_number+1]
                    print ('line: %s' %line)
                    self.images.append(line)
                    line_number += 2
                else:
                    line_number += 1
            print('number of images: %d' %len(self.images))
            print('2d array test 1: %s' %self.images[1][2])
            print('2d array test 2: %s' %self.images[2][len(self.images[2])-2])
            print('2d array test 3: %s' %self.images[1][len(self.images[1])-4])




if __name__=="__main__":
    data = Main('image.data')