import React from "react";
import { axiosReq } from "../../api/axiosDefaults";

const Booking = (props) => {
  const {
    id,
    user,
    is_user,
    profile_id,
    profile_image,
    created_at,
    modified_at,
    event,
    number_of_people,
    add_to_guest,
  } = props;

  const handleSubmit = async (booking) => {
    booking.preventDefault();
    const formData = new FormData();

    formData.append("add to guest", add_to_guest);


    try {
      const { data } = await axiosReq.post("/bookings/", formData);
      history.push(`/bookings/${data.id}`);
    } catch (err) {
      console.log(err);
      if (err.response?.status !== 401) {
        setErrors(err.response?.data);
      }
    }
  };

  return (
    <>
  {add_to_guest ? (
    <Button type="submit">
        Book
      </Button>
  ) : (
    <p>Fully Booked!</p>
  )}
  </>
    );
};

export default Booking;
