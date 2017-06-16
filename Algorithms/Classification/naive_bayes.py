from numpy import genfromtxt, unique, zeros, prod

def Create_Model(data_from_gen, index_classified):
    attributes = data_from_gen[0]
    data = data_from_gen[1:]
    classes = unique(data[:,index_classified])
    model = []
    for index_attr, attr in enumerate(attributes):
        attr = attributes[index_attr]
        model.append([attr])
        attr_occur = unique(data[:,index_attr])
        if index_attr!=index_classified:
            for index_class, c in enumerate(classes):
                attr_data_class = [d[index_attr] for d in data if d[index_classified] == c]
                attr_len = float(len(attr_data_class))
                attr_unique, attr_count = unique(attr_data_class, return_counts=True)
                attr_freq = attr_count/attr_len
                attr_zip = zip(attr_unique, attr_freq)
                model[index_attr].append([c, attr_zip])
                attr_occur_class = unique(attr_data_class)
                diff = list(set(attr_occur) - set(attr_occur_class))
                if len(diff) > 0:
                    zero_freq = zip(diff,zeros(len(diff)))
                    model[index_attr][index_class + 1][1].extend(zero_freq)
        else:
            attr_data_class = data[:,4]
            attr_len = float(len(attr_data_class))
            attr_unique, attr_count = unique(attr_data_class, return_counts=True)
            attr_freq = attr_count/attr_len
            attr_zip = zip(attr_unique, attr_freq)
            model[index_attr].append(attr_zip)
    return model

def Predict(item, model, index_classified):
    i = 1
    result = []
    for name, prob in model[index_classified][1]:
        prob_class = prob
        for index, attr in enumerate(item):
            class_freq = model[index][i][1]
            attr_prob = class_freq[[x[0] for x in class_freq].index(attr)][1]
            prob_class*= attr_prob
        result.append((name, prob_class))
        i=i+1
    return result

def Normalize(result):
    norm_result = []
    prob_sum = sum([x[1] for x in result])
    for name, prob in result:
        norm_result.append((name, prob/prob_sum))
    return norm_result



data_from_gen= genfromtxt('../../Data/weather.csv', delimiter=',', dtype=None)
index_classified = 4 # Column index which contains classes to be classified
item = ["Sunny", "Cool", "High","True"]

model = Create_Model(data_from_gen, index_classified)
prediction = Predict(item, model, index_classified)
norm_prediction = Normalize(prediction)