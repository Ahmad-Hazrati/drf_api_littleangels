import React, { useEffect, useState } from "react";

import Form from "react-bootstrap/Form";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Container from "react-bootstrap/Container";

import appStyles from "../../App.module.css";
import styles from "../../styles/PostsPage.module.css";
import { axiosReq } from "../../api/axiosDefaults";
import Event from "./Event";
import NoResults from "../../assets/no-results.png";
import Asset from "../../components/Asset";

function EventsPage({ message, filter = "" }) {
  const [events, setEvents] = useState({ results: [] });
  const [hasLoaded, setHasLoaded] = useState(false);

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const { data } = await axiosReq(`/events/${filter}`);
        setEvents(data);
        setHasLoaded(true);
      } catch (err) {
        console.log(err);
      }
    };
    setHasLoaded(false);
    fetchEvents();
  }, [filter]);

  return (
    <Row className="h-100">
      <Col className="py-2 p-0 p-lg-2" lg={8}>
        <p>Popular profiles mobile</p>
        {hasLoaded ? (
          <>
            {events.results.length ? (
              events.results.map((event) => <Event key={event.id} />)
            ) : (
              <Container className={appStyles.Content}>
                <Asset src={NoResults} message={message} />
              </Container>
            )}
          </>
        ) : (
          <Container className={appStyles.Content}>
           <Asset /> 
          </Container>
        )}
      </Col>
      <Col md={4} className="d-none d-lg-block p-0 p-lg-2">
        <p>Popular profiles for desktop</p>
      </Col>
    </Row>
  );
}

export default EventsPage;