import React from "react";
import Card from "react-bootstrap/Card";
import Media from "react-bootstrap/Media";
import { Link } from "react-router-dom";
import styles from "../../styles/Post.module.css";

const Event = (props) => {
  const {
    id,
    title,
    description,
    event_image,
    alt_tag,
    venue,
    published,
    eventobjects,
    start_date,
    end_date,
    eventPage,
    setEvents,
  } = props;

  return (
    <Card className={styles.Post}>
      <Card.Header>
        <Card.Title className="text-center">{title}</Card.Title>
      </Card.Header>

      <Card.Body>
        <Link to={`/events/${id}`}>
          <Card.Img src={event_image} alt={alt_tag} />
        </Link>
      </Card.Body>
      <Card.Body>
        <Media className="align-items-center justify-content-between">
          <div>
            <Card.Text>
              <p>{description}</p>
              <p>
                <i className="fas fa-notes-medical"></i> {eventobjects}
              </p>
              <div className="">
                <i className="fas fa-map-marker-alt"></i>{" "}
                <strong>{venue}</strong>
              </div>
              <div>
                <i className="fas fa-calendar-week"></i>
                <strong>{start_date}</strong> till <strong>{end_date}</strong>
              </div>
            </Card.Text>
          </div>
        </Media>
      </Card.Body>
      <Card.Footer className="text-center">
        Published date: {published}
      </Card.Footer>
    </Card>
  );
};

export default Event;
