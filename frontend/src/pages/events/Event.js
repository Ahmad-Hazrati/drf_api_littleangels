import React from "react";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import { Link } from "react-router-dom/cjs/react-router-dom";
import { Overlay, OverlayTrigger, Tooltip } from "react-bootstrap";

const Event = (props) => {
  const {
    id,
    title,
    category,
    excerpt,
    description,
    start_date,
    end_date,
    venue,
    status,
    created_at,
    modified_at,
    slug,
    published,
    guests_registered,
    max_guests,
    user,
    eventPage,
  } = props;

  const currentUser = useCurrentUser();
  const is_user = currentUser?.username === user;

  return (
    <Card className="text-center">
      <Card.Header>{category}</Card.Header>
      <Card.Body>
        <Card.Title>{title}</Card.Title>
        <Card.Text>
          <Link to={`/events/${id}`}>{excerpt}</Link>
          <div></div>
          <div className="d-flex align-items-center">
            <span></span>
            {is_user && eventPage && "..."}
          </div>
        </Card.Text>
        {is_user ? (
          <OverlayTrigger
            placement="top"
            overlay={<Tooltip>You can't book your own event!</Tooltip>}
          ></OverlayTrigger>
        ) : is_user ? (
          <span onClick={() => {}}>Book icon</span>
        ) : currentUser ? (
          <span onClick={() => {}}>book icon</span>
        ) : (
          <OverlayTrigger
            placement="top"
            overlay={<Tooltip>Login to book events!</Tooltip>}
          ></OverlayTrigger>
        )}
        <Button>cancel</Button>
        <Button>Book</Button>
      </Card.Body>
      <Card.Footer className="text-muted">{created_at}</Card.Footer>
    </Card>
  );
};

export default Event;
