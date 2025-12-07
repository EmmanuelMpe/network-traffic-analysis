import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('network_traffic_data.csv')
dataFrame = pd.DataFrame(data)

# Cleaning
dataFrame = dataFrame[dataFrame['Duration'] > 0]

dataFrame['Throughput_Bps'] = dataFrame['ByteCount'] / dataFrame['Duration']

dataFrame['Avg_Packet_Size'] = dataFrame['ByteCount'] / dataFrame['PacketCount']

total_volume_mb = dataFrame['ByteCount'].sum() / 1e6  # Convert to Megabytes
avg_packet_size = dataFrame['Avg_Packet_Size'].mean()
top_protocol = dataFrame.groupby('Protocol')['ByteCount'].sum().idxmax()


# SEABORN VISUALIZATIONS

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.barplot(data=dataFrame, x='Protocol', y='ByteCount', estimator=sum, palette='viridis')
plt.title('Total Bandwidth Consumption by Protocol')
plt.ylabel('Total Bytes')
#plt.savefig('viz1_bandwidth.png')
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(data=dataFrame, x='Duration', y='ByteCount', hue='Label', style='Protocol', s=100)
plt.title('Duration vs. Data Volume')
plt.yscale('log')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=dataFrame,
            x='Protocol',
            y='Throughput_Bps',
            hue='Label')
plt.title('Throughput Stability Analysis (Bytes/Sec)')
plt.show()

#dataFrame.to_csv('cleaned_network_data.csv', index=False)