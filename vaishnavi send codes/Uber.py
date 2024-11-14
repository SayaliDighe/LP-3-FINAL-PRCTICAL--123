import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import datetime as dt

# Load dataset
data = pd.read_csv("uber.csv")
data.head()

# Drop rows with missing dropoff coordinates
data = data.dropna(subset=['dropoff_longitude', 'dropoff_latitude'])

#Haversine distance function to calculate distance between two lat/long points
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371  # Radius of Earth in kilometers
    return c * r

# Calculate distance for each ride in the dataset
data['distance_km'] = data.apply(
    lambda row: haversine(
        row['pickup_latitude'], row['pickup_longitude'],
        row['dropoff_latitude'], row['dropoff_longitude']
    ), axis=1
)

# Convert pickup_datetime to datetime and extract features
data['pickup_datetime'] = pd.to_datetime(data['pickup_datetime'])
data['hour'] = data['pickup_datetime'].dt.hour
data['day_of_week'] = data['pickup_datetime'].dt.dayofweek

# Prepare features and target variable
X = data[['distance_km', 'hour', 'day_of_week', 'passenger_count']]
y = data['fare_amount']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Train a Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Calculate performance metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse}")

# Example Prediction
pickup = (-73.9614469999999, 40.693965)  # Example pickup location
dropoff = (-73.871195, 40.774297) # Example dropoff location
datetime_of_ride = dt.datetime(2024, 10, 12, 7, 4)

# Calculate distance and prepare other features for prediction
distance = haversine(pickup[0], pickup[1], dropoff[0], dropoff[1])
hour = datetime_of_ride.hour
day_of_week = datetime_of_ride.weekday()
passenger_count = 1 # Example passenger count

# Prepare input data for prediction
input_data = scaler.transform([[distance, hour, day_of_week, passenger_count]])

# Predict fare
predicted_fare = model.predict(input_data)
print(f"Predicted Fare: ${predicted_fare[0]:.2f}")