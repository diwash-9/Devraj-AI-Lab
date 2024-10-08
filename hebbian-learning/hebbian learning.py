# -*- coding: utf-8 -*-
"""hebbian.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10DMl8M2kiq6V_yQE93ilfUUEXASIOSqt
"""

import pandas as pd
import numpy as np
class HebbianNeuron(object):
  def __init__(self, shape, learning_rate =1, epoch=1):
      self.shape = shape
      self.learning_rate = learning_rate
      self.epochs = epoch
      self.weights = np.zeros(self.shape)
      self.bias = np.zeros(1)

  def train(self, inputs, targets):
      for epoch in range(self.epochs):
        for i in range(len(inputs)):
          input_pattern = inputs[i]
          target = targets[i]
          output = np.dot(self.weights, input_pattern)
          self.weights += self.learning_rate * target * input_pattern
          self.bias += self.learning_rate * target
          print("Weight updated: " + str(self.weights[0]))
          print("Weight updated: " + str(self.weights[1]))
          print("Bias updated: " + str(self.bias))
          print("----------------------------------------")
      return self.weights, self.bias

  def predict(self, inputs, ret = False):
      self.out_raw =[]
      self.out_val =[]
      for input_pattern in inputs:
        output = input_pattern.dot(self.weights)+self.bias
        self.out_raw.append(output)
        self.out_val.append(1 if output>0 else -1)
        if not ret:
          print(f"Input: {input_pattern}, Output:{output > 0}")

  def TruthTable(self, input, input_labels, output_labels):
    table = pd.DataFrame(input, columns = input_labels)
    self.predict(input,True)
    table[output_labels] = pd.Series(self.out_val)
    return table

inputs = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])
targets = np.array([1, -1, -1, -1])
OR = HebbianNeuron(inputs.shape[1])

OR.train(inputs, targets)

OR.predict(inputs)

OR.out_raw, OR.out_val

inputs = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])
targets = np.array([-1, -1, -1, 1])
AND= HebbianNeuron(inputs.shape[1])

AND.train(inputs, targets)

AND.predict(inputs)

AND.out_raw, AND.out_val

in_labels = ['x1', 'x2']
out_label = 'y'
AND.TruthTable(inputs,in_labels, out_label)

