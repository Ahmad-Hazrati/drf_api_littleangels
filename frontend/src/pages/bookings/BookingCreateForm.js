import React from "react";

import Form from "react-bootstrap/Form";
import Alert from "react-bootstrap/Alert";
import Button from "react-bootstrap/Button";

import btnStyles from "../../styles/Button.module.css";
import { axiosRes } from "../../api/axiosDefaults";
import { useHistory } from "react-router-dom";
import Booking from "./Booking";

const BookingCreateForm = (props) => {
  const { event, setEvent, setBookings } = props;
  const history = useHistory();

  const handleBook = async (e) => {
    e.preventDefault();
    try {
      // don't forget to check bool avillable_seats
      const { data } = await axiosRes.post("/bookings/", { event });
      setBookings((prevBookings) => ({
        ...prevBookings,
        results: [data, ...prevBookings.results],
      }));
      setEvent((prevEvent) => ({
        results: [
          {
            ...prevEvent.results[0],
            bookings_count: prevEvent.results[0].bookings_count + 1,
          },
        ],
      }));
    } catch (err) {
      undefined
    }
  };

  return (
    <Form className="mt-2 text-center" onSubmit={handleBook}>
      <Button
        className={`${btnStyles.Button} ${btnStyles.Wide} ${btnStyles.Bright} my-2`}
        onClick={() => history.goBack()}
      >
        back
      </Button>
      {<Booking available_seats={event.available_seats} /> ? (
        <div>
          <Button
            className={`${btnStyles.Button} ${btnStyles.Wide} ${btnStyles.Bright} my-2`}
            type="submit"
          >
            book
          </Button>
        </div>
      ) : (
        <div>
          <Alert variant="warning">All seats are fully booked!</Alert>
        </div>
      )}
    </Form>
  );
};

export default BookingCreateForm;
