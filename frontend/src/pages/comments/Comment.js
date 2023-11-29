import React from "react";
import styles from "../../styles/Comment.module.css";
import { Link } from "react-router-dom/cjs/react-router-dom";
import Avatar from "../../components/Avatar";
import { Media } from "react-bootstrap";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import { MoreDropdown } from "../../components/MoreDropdown";
import { axiosRes } from "../../api/axiosDefaults";

const Comment = (props) => {
  const {
    profile_id,
    profile_image,
    user,
    modified_at,
    description,
    id,
    setPost,
    setComments,
  } = props;

  const currentUser = useCurrentUser();
  const is_user = currentUser?.username === user;

  const handleDelete = async () => {
    try {
      await axiosRes.delete(`/comments/${id}/`);
      setPost((prevPost) => ({
        results: [
          {
            ...prevPost.results[0],
            comments_count: prevPost.results[0].comments_count - 1,
          },
        ],
      }));
      setComments((prevComments) => ({
        ...prevComments,
        results: prevComments.results.filter((comment) => comment.id !== id),
      }));
    } catch (err) {}
  };

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
        {is_user && (
          <MoreDropdown handleEdit={() => {}} handleDelete={handleDelete} />
        )}
      </Media>
    </div>
  );
};

export default Comment;
