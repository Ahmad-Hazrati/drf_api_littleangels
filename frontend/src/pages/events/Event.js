import React from "react";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import Media from "react-bootstrap/Media";
import Alert from "react-bootstrap/Alert";
import { Link } from "react-router-dom/cjs/react-router-dom";
import btnStyles from "../../styles/Button.module.css";
import styles from "../../styles/Post.module.css";
import { Form } from "react-bootstrap";

const Event = (props) => {
  const {
    id,
    user,
    title,
    excerpt,
    description,
    event_image,
    alt_tag,
    venue,
    published,
    eventobjects,
    max_guests,
    guests_registered,
    max_seats,
    registered_seats,
    available_seats,
    start_date,
    end_date,
    created_at,
    modified_at,
    eventPage,
  } = props;

  const currentUser = useCurrentUser();
  const is_user = currentUser?.username === user;

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
              <div>
                <i className="fas fa-users"></i>
                <strong>Max seats: {max_seats}</strong>
                <i className="fas fa-chair"></i>
                <strong>
                  Booked seats: {registered_seats}
                </strong>
              </div>
              {registered_seats !== max_seats ? (
                <>
                  <div>
                    <Button
                      className={`${btnStyles.Button} ${btnStyles.Blue}`}
                      // onClick={() => history.goBack()}
                    >
                      cancel
                    </Button>
                    <Button
                      className={`${btnStyles.Button} ${btnStyles.Blue}`}
                      type="submit"
                    >
                      book
                    </Button>
                  </div>
                </>
              ) : (
                <Alert variant="warning">All seats are fully booked!</Alert>
              )}
            </Card.Text>
          </div>
        </Media>
      </Card.Body>
      <Card.Footer className="d-flex align-items-center">
        Published date: {published}
      </Card.Footer>
    </Card>
  );
};

export default Event;
