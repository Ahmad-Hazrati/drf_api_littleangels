import React from "react";
import styles from "../../styles/Post.module.css";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import { Card, Media, OverlayTrigger, Tooltip } from "react-bootstrap";
import Avatar from "../../components/Avatar";
import { Link } from "react-router-dom";

const Post = (props) => {
  const {
    id,
    user,
    profile_id,
    profile_image,
    comments_count,
    likes_count,
    like_id,
    title,
    description,
    image,
    modified_at,
    postPage,
  } = props;
  const currentUser = useCurrentUser();
  const is_user = currentUser?.username === user;

  return (
    <Card className={styles.Post}>
      <Card.Body>
        <Media className="align-items-center justify-content-between">
          <Link to={`/profiles/${profile_id}`}>
            <Avatar src={profile_image} height={55} />
            {user}
          </Link>
          <div className="d-flex align-items-center">
            <span>{modified_at}</span>
            {is_user && postPage && "..."}
          </div>
        </Media>
      </Card.Body>
      <Link to={`/posts/${id}`}>
        <Card.Img src={image} alt={title} />
      </Link>
      <Card.Body>
        {title && <Card.Title className="text-center">{title}</Card.Title>}
        {description && <Card.Text>{description}</Card.Text>}
        <div className={styles.PostBar}>
            {is_user ? (
                <OverlayTrigger placement="top" overlay={<Tooltip>You can't like your own post!</Tooltip>}>
                    <i className="far fa-heart" />
                </OverlayTrigger>
            ) : like_id ? (
                <span onClick={()=> {}}>
                    <i className={`fas fa-heart ${styles.Heart}`} />
                </span>
            ) : currentUser ? (
                <span onClick={() => {}}>
                    <i className={`far fa-heart ${styles.HeartOutline}`} />
                </span>
            ) : (
                <OverlayTrigger placement="top" overlay={<Tooltip>Log in to like post!</Tooltip>}>
                    <i className="far fa-heart" />
                </OverlayTrigger>
            )}
            {likes_count}
            <Link to={`/posts/${id}`}>
                <i className="far fa-comments" />
            </Link>
            {comments_count}
        </div>
      </Card.Body>
    </Card>
  );
};

export default Post;
