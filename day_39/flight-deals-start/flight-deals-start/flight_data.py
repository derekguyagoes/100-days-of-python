class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(
            self,
            origin_city,
            origin_airport,
            dest_city,
            dest_airport,
            departure_date,
            return_date,
            price,
    ):
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.dest_city = dest_city
        self.dest_airport = dest_airport
        self.depature_date = departure_date
        self.return_date = return_date
        self.price = price
