#Building a full layer
inputs = [1, 2, 3, 2.5]

weight1 = [0.2, 0.8, -0.5, 1.0]
weight2 = [0.5, -.91, .26, -.5]
weight3 = [-.26, -.27, .17, .87]

biases = [2, 3, .5]

outputs = [
    inputs[0] * weight1[0] + inputs[1] * weight1[1] + inputs[2] * weight1[2] + inputs[3] * weight1[3] + biases[0],
    inputs[0] * weight2[0] + inputs[1] * weight2[1] + inputs[2] * weight2[2] + inputs[3] * weight2[3] + biases[1],
    inputs[0] * weight3[0] + inputs[1] * weight3[1] + inputs[2] * weight3[2] + inputs[3] * weight3[3] + biases[2]
]

print(outputs)