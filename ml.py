import matplotlib.pyplot as plt

def plot_preds(training_data, training_labels, testing_data, testing_labels, preds):
  plt.figure(figsize=(10, 7))
  plt.scatter(training_data, training_labels, c="g", label="Training Data")
  plt.scatter(testing_data, testing_labels, c="b", label="Testing Data")
  plt.scatter(testing_data, preds, c="r", label="Predictions")
  plt.legend()
  plt.show()
