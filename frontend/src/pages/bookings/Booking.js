import React from "react";
import Media from "react-bootstrap/Media";
import Card from "react-bootstrap/esm/Card";
import { Link } from "react-router-dom";
import Avatar from "../../components/Avatar";
import { MoreDropdownBooking } from "../../components/MoreDropdown";
import Alert from "react-bootstrap/esm/Alert";

import styles from "../../styles/Comment.module.css";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import { axiosRes } from "../../api/axiosDefaults";

const Booking = (props) => {
  const {
    id,
    profile_id,
    profile_image,
    user,
    modified_at,
    setEvent,
    setBookings,
  } = props;

  const currentUser = useCurrentUser();
  const is_user = currentUser?.username === user;

  const handleDeleteConfirmation = () => {
    if (window.confirm("Are you sure you want to delete this booking?")) {
      handleDeleteBooking();
    }
  };

  const handleDeleteBooking = async () => {
    try {
      await axiosRes.delete(`/bookings/${id}/`);
      setEvent((prevEvent) => ({
        results: [
          {
            ...prevEvent.results[0],
            bookings_count: prevEvent.results[0].bookings_count - 1,
          },
        ],
      }));

      setBookings((prevBookings) => ({
        ...prevBookings,
        results: prevBookings.results.filter((booking) => booking.id !== id),
      }));
    } catch (err) {
      undefined;
    }
  };

  return (
    <>
      <Card className={`${styles.Post} my-2`}>
        <Card.Body>
          <Media className="align-items-center justify-content-between">
            <Link to={`/profiles/${profile_id}`}>
              <Avatar src={profile_image} height={55} />
              {user}
            </Link>
            <div className="d-flex align-items-center">
              <span>{modified_at}</span>
              {is_user ? (
                <MoreDropdownBooking
                  handleDeleteBooking={handleDeleteConfirmation}
                />
              ) : (
                <div>
                  <Alert variant="warning">
                    You are not the authorized user to delete this booking
                  </Alert>
                </div>
              )}
            </div>
          </Media>
        </Card.Body>
      </Card>
    </>
  );
};

export default Booking;
