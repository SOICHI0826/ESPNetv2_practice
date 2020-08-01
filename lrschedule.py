# -*- coding: utf-8 -*-
"""LRSchedule.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R9GUFKcQ7oIm6sMbiUFkRDCVXEV7Y71Q
"""

class LRScheduler(object):
  def __init__(self, initial = 0.1, cycle_len = 5, steps = [51, 101, 131, 161, 191, 221, 251, 281], gamma = 2):
    super(LRScheduler, self).__init__()
    self.min_lr = initial
    self.cycle = cycle_len
    self.steps = steps
    self.counter = 0
    self.decayFactor = gamma
    self.count_cycles = 0
    self.step_counter = 0
    self.stepping = True
  
  def get_lr(self, epoch):
    if  epoch % self.steps[self.step_counter] == 0 and epoch > 1 and self.stepping:
      self.min_lr = self.min_lr / self.decayFactor
      self.count_cycles = 0
      if self.step_counter < len(self.steps) - 1:
        self.step_counter += 1
      else:
        self.stepping = False
    count_lr = self.min_lr
    #warm restarts
    if epoch == 1:
      current_lr = current_lr
    else:
      if self.counter >= self.cycle:
        self.counter = 0
      current_lr = round((self.min_lr * self.cycle) - (self.counter * self.min_lr), 5)
      self.counter += 1
      self.count_cycles += 1

    return current_lr