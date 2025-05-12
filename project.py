import matplotlib.pyplot as plt

# Assume these are the MAPE values you calculated from your models
# Replace with your actual values if different
mape = 0.10  # Replace with your LSTM MAPE
mape_rnn = 0.15  # Replace with your RNN MAPE
mape_cnn = 0.12  # Replace with your CNN MAPE (this should be calculated similarly to mape and mape_rnn)

mape_scores = [mape, mape_rnn, mape_cnn]
models = ['LSTM', 'RNN', 'CNN']

# Create the bar chart
plt.figure(figsize=(6, 4))
plt.bar(models, mape_scores, color=['blue', 'green', 'orange'])

# Add labels and title
plt.title('MAPE Comparison for LSTM, RNN, and CNN', fontsize=14)
plt.xlabel('Models', fontsize=12)
plt.ylabel('MAPE (%)', fontsize=12)

# Show the MAPE values on top of the bars
for i, v in enumerate(mape_scores):
    plt.text(i, v + 0.1, f'{v:.2f}%', fontsize=12)

# Display the plot
plt.show()