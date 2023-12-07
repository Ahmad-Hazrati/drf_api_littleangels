import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import btnStyles from "../../styles/Button.module.css"
import { useHistory } from "react-router-dom";
import { axiosRes } from "../../api/axiosDefaults";

const Booking = (props) => {
  const { id, created_at, modified_at, setEvent, setBookings } =
    props;
  console.log(props);

  const history = useHistory();
  const [errors, setErrors] = useState({});

  const handleDeleteBooking = async () => {
    try {
      await axiosRes.delete(`/bookings/${id}/`);
      setEvent((prevEvent) => ({
        results: [
          {
            ...prevEvent.results[0],
            Bookings_count: prevEvent.results[0].Bookings_count - 1,
          },
        ],
      }));

      setBookings((prevBookings) => ({
        ...prevBookings,
        results: prevBookings.results.filter((booking) => booking.id !== id),
      }));
    } catch (err) {}
  };


  return (
    <>
      <hr />
      <div>
            <Button
              className={`${btnStyles.Button} ${btnStyles.Blue}`}
              type="submit"
            >
              Cancel booking
            </Button>
          </div>
    </>
  );
};

export default Booking;
