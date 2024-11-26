# Import dependencies
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
import datetime as dt

# Database setup
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# References to tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session link
Session = sessionmaker(bind=engine)
session = Session()

# Flask app setup
app = Flask(__name__)

# Flask routes
@app.route("/")
def welcome():
    """List all available API routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the last 12 months of precipitation data as JSON."""
    # Get the most recent date in the dataset
    latest_date = session.query(func.max(Measurement.date)).scalar()
    latest_date = dt.datetime.strptime(latest_date, '%Y-%m-%d')
    one_year_ago = latest_date - dt.timedelta(days=365)

    # Query for the precipitation data
    prcp_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()

    # Convert to dictionary
    prcp_dict = {date: prcp for date, prcp in prcp_data}
    return jsonify(prcp_dict)

@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations."""
    station_data = session.query(Station.station, Station.name).all()
    station_list = [{"station": station, "name": name} for station, name in station_data]
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return temperature observations of the most active station for the last year."""
    # Identify the most active station
    most_active_station = session.query(Measurement.station).group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()[0]

    # Get the most recent date in the dataset
    latest_date = session.query(func.max(Measurement.date)).scalar()
    latest_date = dt.datetime.strptime(latest_date, '%Y-%m-%d')
    one_year_ago = latest_date - dt.timedelta(days=365)

    # Query temperature observations for the most active station
    tobs_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == most_active_station).\
        filter(Measurement.date >= one_year_ago).all()

    # Convert to list of temperature observations
    tobs_list = [{"date": date, "temperature": tobs} for date, tobs in tobs_data]
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def stats(start, end=None):
    """Return TMIN, TAVG, and TMAX for a specified start or start-end range."""
    if not end:
        # Query for stats from start date onward
        stats_data = session.query(func.min(Measurement.tobs),
                                   func.avg(Measurement.tobs),
                                   func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).all()
    else:
        # Query for stats between start and end dates
        stats_data = session.query(func.min(Measurement.tobs),
                                   func.avg(Measurement.tobs),
                                   func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    # Convert to JSON
    stats_list = [{"TMIN": tmin, "TAVG": tavg, "TMAX": tmax} for tmin, tavg, tmax in stats_data]
    return jsonify(stats_list)

if __name__ == "__main__":
    app.run(debug=True)
