#Building a full layer
inputs = [1, 2, 3, 2.5]
 
weights = [
    [0.2, 0.8, -0.5, 1.0 ],
    [0.5, -.91, .26, -.5 ],
    [-.26, -.27, .17, .87]
] 
biases = [2, 3, .5]

layer_outputs = []
for neuron_weights, neuron_bais in zip(weights, biases):
    neuron_output = 0
    for neuorn_input, weight in zip(inputs, neuron_weights):
        neuron_output += neuorn_input * weight
    neuron_output += neuron_bais
    layer_outputs.append(neuron_output)

print(layer_outputs)