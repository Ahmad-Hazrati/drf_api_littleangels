import React, { useEffect, useState } from "react";

import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Container from "react-bootstrap/Container";

import appStyles from "../../App.module.css";
import { useParams } from "react-router-dom";
import { axiosReq } from "../../api/axiosDefaults";
import Event from "./Event";
import BookingCreateForm from "../bookings/BookingCreateForm";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import PopularProfiles from "../profiles/PopularProfiles";
import Booking from "../bookings/Booking";

function EventPage() {
  const { id } = useParams();
  const [event, setEvent] = useState({ results: [] });

  const currentUser = useCurrentUser();
  const profile_image = currentUser?.profile_image;
  const [bookings, setBookings] = useState({ results: [] });

  useEffect(() => {
    const handleMount = async () => {
      try {
        const [{ data: event }, { data: bookings }] = await Promise.all([
          axiosReq.get(`/events/${id}`),
          axiosReq.get(`/bookings/?event=${id}`),
        ]);
        setEvent({ results: [event] });
        setBookings(bookings);
      } catch (err) {
      }
    };
    handleMount();
  }, [id]);

  return (
    <Row className="h-100">
      <Col className="py-2 p-0 p-lg-2" lg={8}>
        <PopularProfiles mobile />
        <Event {...event.results[0]} setEvents={setEvent} eventPage />
        <Container className={appStyles.Content}>
          {currentUser ? (
            <BookingCreateForm
              profile_id={currentUser.profile_id}
              profileImage={profile_image}
              event={id}
              setEvent={setEvent}
              setBookings={setBookings}
            />
          ) : bookings.results.length ? (
            "Bookings"
          ) : null}
          {bookings.results.length ? (
            bookings.results.map((booking) => (
              <Booking
                key={booking.id}
                {...booking}
                setEvent={setEvent}
                setBookings={setBookings}
              />
            ))
          ) : currentUser ? (
            <span>No bookings yet, be the first to book!</span>
          ) : (
            <span>No booking... yet</span>
          )}
        </Container>
      </Col>
      <Col lg={4} className="d-none d-lg-block p-0 p-lg-2">
        <PopularProfiles />
      </Col>
    </Row>
  );
}

export default EventPage;
