from Classify import Classify

class Main (object):
    def __init__(self, perceptron_file):
        self.images = list()
        with open (perceptron_file) as f:
            lines = f.readlines()
            line_number = 0;
            while line_number < len(lines):
                if len(lines[line_number]) > 10:
                    line = lines[line_number].rstrip() + lines[line_number+1].rstrip()
                    start_break_point = 0
                    end_break_point = 10
                    self.image = list()
                    while end_break_point <= len(line):
                        image_row = line[start_break_point:end_break_point]
                        self.image.append(image_row)
                        end_break_point += 10
                        start_break_point += 10
                    self.images.append(self.image)
                    line_number += 2
                else:
                    line_number += 1
if __name__=="__main__":
    data = Main('image.data')

    Classify(data)