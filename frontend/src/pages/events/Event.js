import React from "react";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import Media from "react-bootstrap/Media";
import { Link } from "react-router-dom/cjs/react-router-dom";
import btnStyles from "../../styles/Button.module.css";
import styles from "../../styles/Post.module.css";
import { Form } from "react-bootstrap";

const Event = (props) => {
  const {
    id,
    title,
    excerpt,
    description,
    event_image,
    alt_tag,
    venue,
    published,
    eventobjects,
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
      <Link to={`/events/${id}`}>
        <Card.Header>
          <Card.Title className="text-center">{title}</Card.Title>
        </Card.Header>
      </Link>
      <Card.Body>
        <Media className="align-items-center justify-content-between">
          <Card.Text>
            <p>{description}</p>
            <div>
              <span>
                <i className="fas fa-map-marker-alt"></i>{" "}
                <strong>{venue}</strong>
              </span>
              <span>
                <i className="fas fa-calendar-week"></i>
                <strong>{start_date}</strong> till <strong>{end_date}</strong>
              </span>
            </div>
            <div>
              <span>
                <i className="fas fa-users"></i>
                <strong>{max_guests}</strong>
              </span>
              <span>
                Registered:<strong>{guests_registered}</strong>
              </span>
            </div>
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
          </Card.Text>
        </Media>
      </Card.Body>
      <Card.Footer className="d-flex align-items-center">
        Created date: {created_at} modified date: {modified_at}
      </Card.Footer>
    </Card>
  );
};

export default Event;
