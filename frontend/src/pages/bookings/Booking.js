import React from "react";
import Media from "react-bootstrap/Media";
import { Link } from "react-router-dom";
import Avatar from "../../components/Avatar";
import { MoreDropdown } from "../../components/MoreDropdown";

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
  // user is undefined => you are not sending this data
  console.log("profile_id: ", profile_id);
  console.log("booking id: ", id);
  console.log("props: ", props);
  console.log("currentUser: ", currentUser);
  console.log("currentUser.pk: ", currentUser.pk);
  const is_user = currentUser.pk === profile_id;
  console.log("is_user", is_user);

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
      <Media>
        <Link to={`/profiles/${profile_id}`}>
          <Avatar src={profile_image} />
        </Link>
        <Media.Body className="align-self-center ml-2">
          <span className={styles.Owner}>{user}</span>
          <span className={styles.Date}>{modified_at}</span>
        </Media.Body>
        {is_user ? (
          <MoreDropdown handleDelete={handleDeleteBooking} />
        ) : (
          <p>You are not the authorized user to delete this booking</p>
        )}
      </Media>
    </>
  );
};

export default Booking;
