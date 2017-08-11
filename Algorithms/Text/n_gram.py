input = "The cow jumps over the moon"
n=2

# pre-processing:
stop_list=["a", "an", "the", "as", "while", "with"]
input = input.lower()
for word in stop_list:
    input= input.replace(word, "")
print input


tokens = input.split()
tokens_len = len(tokens)
output = []
for start, token in enumerate(tokens):
    end = start+ n
    if(end <= tokens_len):
        t = ""
        for i in xrange(start,end):
            t += tokens[i] + " "
        output.append(t)

print "tokens:"
for token in output:
    print "* " + token