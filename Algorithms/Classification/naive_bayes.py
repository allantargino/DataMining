from numpy import genfromtxt, unique

data = genfromtxt('../../Data/IPR_filtered.csv', delimiter=',', skip_header=1, dtype=None)
predict = ['Events - Organization', 'Microsoft Azure - Infra']

names=unique(data[:,2])
technologies = unique(data[:,1])
for name in names:
    technology = [t[1] for t in data if t[2] == name]
    count = float(len(technology))
    tech_unique, tech_count = unique(technology, return_counts=True)
    tech_freq = tech_count/count
  
    # activity = [t[0] for t in data if t[2] == name]
    # print name


#['altargin@microsoft.com', ['Events', 0.001], ['Azure', 0.020 ]