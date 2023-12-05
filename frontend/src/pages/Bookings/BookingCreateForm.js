import React, { useState } from "react";
import { Link, useHistory } from "react-router-dom";

import Form from "react-bootstrap/Form";
import Alert from "react-bootstrap/Alert";
import Button from "react-bootstrap/Button";
import InputGroup from "react-bootstrap/InputGroup";

import styles from "../../styles/CommentCreateEditForm.module.css";
import btnStyles from "../../styles/Button.module.css";
import Avatar from "../../components/Avatar";
import { axiosRes } from "../../api/axiosDefaults";
import { useCurrentUser } from "../../contexts/CurrentUserContext";

const BookingCreateForm = (props) => {
  const {
    id,
    user,
    profile_id,
    profileImage,
    created_at,
    modified_at,
    event,
    number_of_people,
    add_to_guest,
    available_seats,
    setEvents,
  } = props;
  const currentUser = useCurrentUser();
  const is_user = currentUser?.username === user;
  const history = useHistory();

  const handleBooking = async () => {
    try {
      const { data } = await axiosRes.post("/bookings/", { event: id });
      setEvents((prevEvents) => ({
        ...prevEvents,
        results: prevEvents.results.map((event) => {
          return event.id === id
            ? {
                ...event,
                number_of_people: number_of_people +1,
                booking_id: data.id,
              }
            : event;
        }),
      }));
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <Form className="mt-2">
      <Form.Group>
        <InputGroup>
          <Link to={`/profiles/${profile_id}`}>
            <Avatar src={profileImage} />
          </Link>
          <Form.Text className="text-muted">
            For booking please fill the required fields!
          </Form.Text>
        </InputGroup>
      </Form.Group>
      {available_seats ? (
        <>
          <div>
            <Button
              className={`${btnStyles.Button} ${btnStyles.Blue}`}
              onClick={() => history.goBack()}
            >
              cancel
            </Button>
            <Button
              className={`${btnStyles.Button} ${btnStyles.Blue}`}
              type="submit"
              onClick={handleBooking}
            >
              book
            </Button>
          </div>
        </>
      ) : (
        <Alert variant="warning">All seats are fully booked!</Alert>
      )}
      {/* <p>Booking Count: {bookings_count}</p> */}
    </Form>
  );
};

export default BookingCreateForm;
