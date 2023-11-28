import React from "react";
import styles from "../../styles/Comment.module.css";
import { Link } from "react-router-dom/cjs/react-router-dom";
import Avatar from "../../components/Avatar";
import { Media } from "react-bootstrap";

const Comment = (props) => {
  const { profile_id, profile_image, user, modified_at, description } = props;

  return (
    <div>
      <hr />
      <Media>
        <Link to={`/profiles/${profile_id}`}>
          <Avatar src={profile_image} />
        </Link>
        <Media.Body>
          <span className={styles.User}>{user}</span>
          <span className={styles.Date}>{modified_at}</span>
          <p>{description}</p>
        </Media.Body>
      </Media>
    </div>
  );
};

export default Comment;
