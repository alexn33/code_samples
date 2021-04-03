import iio
print(iio.version)

import adi
# Create radio object
sdr = adi.Pluto()
# Configure properties
sdr.rx_rf_bandwidth = 4000000
# Get data
data = sdr.rx()
print(data)
